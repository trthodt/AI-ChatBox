from pydantic import BaseModel
from sqlalchemy import Column, DateTime, String
from app.core.database import Base

class ChatBoxRequest(BaseModel):
  content: str

class ChatBoxResponse(BaseModel):
  text: str

class ChatHistory(Base):

  __tablename__ = "chat_history"

  id = Column(String, primary_key=True, index=True)
