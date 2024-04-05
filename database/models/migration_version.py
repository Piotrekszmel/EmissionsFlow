from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone

Base = declarative_base()

class MigrationVersion(Base):
    __tablename__ = 'migration_version'

    id = Column(Integer, primary_key=True)
    version = Column(Integer, nullable=False)
    applied_at = Column(DateTime, default=datetime.now(timezone.utc))