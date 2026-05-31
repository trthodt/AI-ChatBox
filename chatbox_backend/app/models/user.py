import uuid
from sqlalchemy import Column, String, Boolean
from datetime import datetime, timezone
from app.core.database import Base


class User(Base):

  __tablename__ = "user"

  id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
  username = Column(String, unique=True)
  password = Column(String)
  is_deleted = Column(Boolean, default=lambda: False)
  created_at = Column(String, default=lambda: str(int(datetime.now(timezone.utc).timestamp())))
  updated_at = Column(String, default=lambda: str(int(datetime.now(timezone.utc).timestamp())))
