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
  
  def create_new_chat(self, history_id: str, is_user: bool, content: str, db: Session) -> Chat:

    # exist_history = self.get_history_by_id()
    chat = Chat(
      history_id=history_id,
      is_user_chat=is_user,
      chat_content=content,
    )

    db.add(chat)
    db.commit()
    return chat
