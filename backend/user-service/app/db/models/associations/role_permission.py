from sqlalchemy import Table, Column, Integer, ForeignKey, CheckConstraint
from app.db.models import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship


class RolePermission(Base):
    __tablename__ = "role_permission_association"

    role_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True
    )
    permission_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("permissions.id", ondelete="CASCADE"),
        primary_key=True,
    )

    role = relationship("Role", back_populates="role_permission_association")
    permission = relationship(
        "Permission", back_populates="role_permission_association"
    )
