from sqlalchemy.orm import Mapped, mapped_column, relationship, validates
from sqlalchemy import Integer, String, Enum, Boolean
from app.db.models import Base
from app.db.models.permission import Permission
from app.db.models.associations.role_permission import RolePermission
import enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.db.models.user import User


class RoleType(enum.Enum):
    EXECUTOR = "исполнитель"
    CLIENT = "клиент"


class Role(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    role_type: Mapped[RoleType] = mapped_column(Enum(RoleType), nullable=False)
    abbreviation = mapped_column(String(10), nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    is_call_center_operator = mapped_column(Boolean, default=False)

    # Для исполнителей
    edit_comment_time_limit: Mapped[int] = mapped_column(Integer, default=0)
    rate: Mapped[int] = mapped_column(Integer, default=0)
    refresh_time: Mapped[int] = mapped_column(Integer, default=0)

    users: Mapped[list["User"]] = relationship(
        "User", back_populates="role", passive_deletes=True
    )

    # role_permissions = relationship("RolePermission", back_populates="role")

    @validates("id")
    def validate_deletion(self, key, value):
        if any(user.role_id == value for user in self.users):
            raise ValueError("Нельзя удалить роль, пока есть пользователь с этой ролью")
        return value
