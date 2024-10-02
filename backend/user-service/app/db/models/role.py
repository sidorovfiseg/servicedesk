from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from app.db.models import Base
from app.db.models.permission import Permission
from app.db.models.role_permission_association import role_permission_association_table

class Role(Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    
    permissions: Mapped[list['Permission']] = relationship(
        'Permission',
        secondary=role_permission_association_table,
        back_populates='roles'
    )