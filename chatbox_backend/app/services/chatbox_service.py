from sqlalchemy.orm import Session
from google import genai
from app.core.setting import settings

class ChatboxService():

  client: genai.Client

  def __init__(self):
    try:
      api_key = settings.API_KEY
      self.client = genai.Client(api_key=api_key)
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