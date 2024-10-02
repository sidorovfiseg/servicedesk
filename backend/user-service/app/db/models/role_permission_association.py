from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db.models import Base


role_permission_association_table = Table(
    "role_permission_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("role_id", ForeignKey("roles.id"), nullable=False),
    Column("permission_id", ForeignKey("permissions.id"), nullable=False)
)