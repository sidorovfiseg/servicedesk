from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from app.db.models.base import Base
from typing import TYPE_CHECKING
import uuid

if TYPE_CHECKING:
    from db.models.user import User


class Phone(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    phone_number: Mapped[str] = mapped_column(
        String, unique=True, nullable=False, index=True
    )
    is_primary: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_notification_phone: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="phones")
