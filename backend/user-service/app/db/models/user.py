from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Text, ForeignKey, Integer, Boolean
from sqlalchemy.dialects.postgresql import UUID
from typing import Optional
import uuid
from app.db.models import Base
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from db.models.phone import Phone
    from db.models.role import Role


class User(Base):
    id: Mapped[uuid.UUID] = mapped_column(
        UUID, primary_key=True, default=uuid.uuid4, unique=True, index=True
    )
    name: Mapped[str] = mapped_column(String, nullable=False)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    hash_password: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True, nullable=False)

    # Должность
    job_title: Mapped[Optional[str]] = mapped_column(String(60), nullable=True)
    profile_photo: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    description: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    archival: Mapped[bool] = mapped_column(Boolean)
    # Системная роль
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)

    role: Mapped["Role"] = relationship("Role", back_populates="users")
    phones: Mapped[list["Phone"]] = relationship(
        "Phone", back_populates="user", cascade="all, delete-orphan"
    )
