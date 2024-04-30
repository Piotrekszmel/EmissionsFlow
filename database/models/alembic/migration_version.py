from sqlalchemy import Column, Integer, DateTime
from datetime import datetime, timezone

from database.models.alembic.base import Base


class MigrationVersion(Base):
    __tablename__ = 'migration_version'

    id = Column(Integer, primary_key=True)
    version = Column(Integer, nullable=False)
    applied_at = Column(DateTime, default=datetime.now(timezone.utc))