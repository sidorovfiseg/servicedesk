from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    BackgroundTasks,
    status,
    Response,
    Request,
    Query,
    Body,
)
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

# from common.db import db_helper
# from common.settings.logger import logger
# from common.utils.token_helper import token_helper
# from auth.crud.user import UserCRUD
# from auth.security import password_helper, url_helper
# from auth.email import email_service
# from auth.schemas.user import UserCreate, UserUpdate, UserAuth, UserResponse
# from common.utils.deps import get_current_user_id
import uuid
from pydantic import EmailStr

ACCESS_TOKEN_MAX_AGE = 3600
REFRESH_TOKEN_MAX_AGE = 604800

router = APIRouter(tags=["auth"])


@router.post("/register", response_model=dict, status_code=status.HTTP_201_CREATED)
async def register_user(
    user_data: UserCreate,
    background_task: BackgroundTasks,
    session: AsyncSession = Depends(db_helper.get_async_session),
):
    user_crud = UserCRUD(session)
    existing_user = await user_crud.get_user_by_email(user_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already registered")

    user_data.password = password_helper.get_password_hash(user_data.password)

    user = await user_crud.create_user(user_data)

    background_task.add_task(
        email_service.send_confirmation_email,
        user_data.email,
        url_helper.generate_confirmation_url(user.id),
    )

    return {"status": "User created successfuly"}


# Допустим это работает
@router.get("/activate")
async def activate_email(
    response: Response,
    token: str = Query(...),
    session: AsyncSession = Depends(db_helper.get_async_session),
):
    user_crud = UserCRUD(session)
    try:
        payload = token_helper.decode_token(token)
        user_id = uuid.UUID(payload.get("sub"))
        user = await user_crud.get_user(user_id)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
            )

        if user.is_verified:
            return {"message": "Email is already verified"}

        user_update = UserUpdate(is_verified=True)
        user = await user_crud.update_user(user_id, user_update)
        logger.info(f"user -- is_verified - {user.is_verified}")
        access_token = token_helper.create_access_token({"sub": str(user.id)})
        refresh_token = token_helper.create_refresh_token({"sub": str(user.id)})

        response.set_cookie(key="access_token", value=access_token, httponly=True)
        response.set_cookie(key="refresh_token", value=refresh_token, httponly=True)

        return RedirectResponse(url="http://localhost:8000")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token"
        )


@router.post("/send-verification-email")
async def send_verification_email(
    background_task: BackgroundTasks,
    email: EmailStr = Body(..., embed=True),
    session: AsyncSession = Depends(db_helper.get_async_session),
):
    user_crud = UserCRUD(session)
    user = await user_crud.get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if user.is_verified:
        raise HTTPException(status_code=400, detail="User email already verified")

    background_task.add_task(
        email_service.send_confirmation_email,
        user.email,
        url_helper.generate_confirmation_url(user.id),
    )

    return {"message": "Verification email sent successfully"}


@router.post("/send-reset-password-email")
async def reset_password(
    background_task: BackgroundTasks,
    email: EmailStr = Body(..., embed=True),
    session: AsyncSession = Depends(db_helper.get_async_session),
):
    user_crud = UserCRUD(session)
    user = await user_crud.get_user_by_email(email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    random_password = password_helper.generate_random_password()
    user_data = UserUpdate(
        new_password=password_helper.get_password_hash(random_password),
        is_verified=True,
    )
    user = await user_crud.update_user(user.id, user_data)

    background_task.add_task(
        email_service.send_reset_password_email, email, random_password
    )

    return {"message": "Password reset email send successfully"}


@router.post("/update-password")
async def update_password(
    request: Request, session: AsyncSession = Depends(db_helper.get_async_session)
):
    pass


@router.post("/login", response_model=dict)
async def login(
    user_data: UserAuth,
    response: Response,
    session: AsyncSession = Depends(db_helper.get_async_session),
):
    user_crud = UserCRUD(session)
    user = await user_crud.get_user_by_email(user_data.email)
    if not user or not password_helper.verify_password(
        user_data.password, user.password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )
    if not user.is_verified:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Email not confirmed"
        )

    access_token = token_helper.create_access_token(data={"sub": str(user.id)})
    refresh_token = token_helper.create_refresh_token(data={"sub": str(user.id)})

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        max_age=ACCESS_TOKEN_MAX_AGE,
    )
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        samesite="lax",
        max_age=REFRESH_TOKEN_MAX_AGE,
    )

    return {"message": "login successfull"}


@router.post("/token/refresh", response_model=dict)
async def refresh_access_token(request: Request, response: Response):
    refresh_token = request.cookies.get("refresh_token")

    if not refresh_token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Refresh token not provided"
        )

    try:
        payload = token_helper.decode_token(refresh_token)
        user_id = payload.get("sub")

        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Invalid refresh token"
            )

        access_token = token_helper.create_access_token({"sub": str(user_id)})
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            max_age=ACCESS_TOKEN_MAX_AGE,
        )

        return {"message": "Access token refreshed successfully"}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Invalid refresh token"
        )


@router.get("/users/me")
async def get_user_info(
    requst: Request,
    user_id: str = Depends(get_current_user_id),
    session: AsyncSession = Depends(db_helper.get_async_session),
):
    user_crud = UserCRUD(session)

    user = await user_crud.get_user(user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    return UserResponse(email=user.email)
