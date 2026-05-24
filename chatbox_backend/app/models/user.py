from sqlalchemy import Column, String, DateTime, Boolean
from datetime import datetime
from app.core.database import Base


class User(Base):

  __tablename__ = "user"

  id = Column(String, primary_key=True, index=True)
  username = Column(String, unique=True)
  password = Column(String)
  email = Column(String, unique=True)
  is_deleted = Column(Boolean, default=False)
  created_at = Column(DateTime, default=datetime.now())
  updated_at = Column(DateTime, default=datetime.now())
