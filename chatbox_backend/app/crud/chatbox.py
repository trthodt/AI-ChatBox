from sqlalchemy.orm import Session
from app.models.user import User
from app.models.chatbox import ChatHistory, Chat
from app.schemas.user import RegisterRequest
from passlib.context import CryptContext

class ChatboxRepository():

  def get_history_by_id(self, history_id: str, user_id, db: Session) -> ChatHistory:

    chat_history = (
      db.query(ChatHistory)
      .filter(ChatHistory.id == history_id)
      .filter(ChatHistory.user_id == user_id)
      .first()
    )
    
    return chat_history

  def create_chat_history(self, user_id: str, title: str, db: Session):

    new_history = ChatHistory(
      user_id=user_id,
      title=title,
    )

    db.add(new_history)
    db.commit()

    return new_history