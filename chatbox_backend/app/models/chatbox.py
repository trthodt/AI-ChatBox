import uuid
from sqlalchemy import Column, String, Boolean
from datetime import datetime, timezone
from app.core.database import Base


class ChatHistory(Base):

  __tablename__ = "chat_history"

  id = Column(String, primary_key=True, index=True, default=str(uuid.uuid4()))
  user_id = Column(String)
  is_deleted = Column(Boolean, default=False)
  created_at = Column(String, default=str(int(datetime.now(timezone.utc).timestamp())))
  updated_at = Column(String, default=str(int(datetime.now(timezone.utc).timestamp())))


class Chat(Base):

  __tablename__ = "chat"

  id = Column(String, primary_key=True, index=True, default=str(uuid.uuid4()))
  history_id = Column(String)
  is_deleted = Column(Boolean, default=False)
  is_user_chat = Column(Boolean)
  is_send_success = Column(Boolean)
  chat_content = Column(String)
  created_at = Column(String, default=str(int(datetime.now(timezone.utc).timestamp())))
  updated_at = Column(String, default=str(int(datetime.now(timezone.utc).timestamp())))