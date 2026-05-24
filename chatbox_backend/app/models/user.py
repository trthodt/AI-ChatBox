from sqlalchemy import Column, String, Boolean
from datetime import datetime, timezone
from app.core.database import Base


class User(Base):

  __tablename__ = "user"

  id = Column(String, primary_key=True, index=True)
  username = Column(String, unique=True)
  password = Column(String)
  is_deleted = Column(Boolean, default=False)
  created_at = Column(String, default=str(int(datetime.now(timezone.utc).timestamp())))
  updated_at = Column(String, default=str(int(datetime.now(timezone.utc).timestamp())))
