from dotenv import load_dotenv
import os

class Settings():

  API_KEY: str
  POSTGRES_USER: str
  POSTGRES_PASSWORD: str
  DB_URL: str
  MODEL_NAME: str

  def __init__(self):
    load_dotenv()

    self.API_KEY: str = os.getenv('API_KEY')
    self.POSTGRES_USER: str = os.getenv('POSTGRES_USER')
    self.POSTGRES_PASSWORD: str = os.getenv('POSTGRES_PASSWORD')
    self.DB_URL: str = os.getenv('DB_URL')
    self.MODEL_NAME: str = os.getenv('MODEL_NAME')

settings = Settings()