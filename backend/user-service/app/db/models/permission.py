from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Enum
from app.db.models import Base
from app.db.models.associations.role_permission import RolePermission
from typing import TYPE_CHECKING
import enum


class PermisssionType(enum.Enum):
    EXECUTOR = "исполнитель"
    CLIENT = "клиент"
    ALL = "клиент+исполнитель"


class AccessLevel(enum.Enum):
    ONLY_OWN = 0
    OWN_DEPARTMENT = 1
    OWN_DEPARTMENT_WITH_CHILD = 2
    OWN_COMPANY = 3
    ALL = 4


if TYPE_CHECKING:
    from app.db.models.role import Role


class Permission(Base):

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    permission_type: Mapped[PermisssionType] = mapped_column(
        Enum(PermisssionType), nullable=False
    )
    description: Mapped[str] = mapped_column(String, nullable=True)
    access_level: Mapped[AccessLevel] = mapped_column(
        Enum(AccessLevel), default=AccessLevel.ONLY_OWN
    )

    role_permissions = relationship("RolePermission", back_populates="permission")
