from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from google import genai
from app.core.setting import settings
from app.crud.chatbox import ChatboxRepository
from app.models.chatbox import  ChatHistory, Chat

class ChatboxService():

  client: genai.Client
  chatbox_repository: ChatboxRepository

  def __init__(self):
    try:
      api_key = settings.API_KEY
      self.client = genai.Client(api_key=api_key)
      self.chatbox_repository = ChatboxRepository()
    except Exception as e:
      print(e.__class__)
      print(e)


  def run_model(self, chat_content: str, db: Session):
    try:
      response = self.client.models.generate_content(
      model=settings.MODEL_NAME, 
      contents=chat_content,
      config={
        "system_instruction": "Hãy nói tiếng Việt trong mọi đoạn chat.",
      }
      )
      return response.text
    except Exception as e:
      print(e.__class__)
      print(e)
      raise e
  
  def create_chat_history(self, user_id: str, chat_title: str, db: Session) -> ChatHistory:

    new_history = self.chatbox_repository.create_chat_history(user_id, chat_title, db)
    return new_history

  def get_history_by_id(self, history_id: str, user_id: str, db: Session) -> ChatHistory | None:
    history = self.chatbox_repository.get_history_by_id(history_id, user_id, db)

    if not history:
      return None
    
    return history
  
  def create_new_chat(self, history_id: str, is_user: bool, chat_content: str, db: Session) -> Chat:

    self.chatbox_repository.create_new_chat(history_id, is_user=is_user, content=chat_content, db=db)