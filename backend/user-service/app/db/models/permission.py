from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from app.db.models import Base
from app.db.models.role_permission_association import role_permission_association_table
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.db.models.role import Role

class Permission(Base):
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    
    roles: Mapped[list['Role']] = relationship(
        'Role',
        secondary=role_permission_association_table,
        back_populates="permissions"
    )