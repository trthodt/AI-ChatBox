from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.core.setting import Settings
from app.utils.exception_handle import exception_handler

settings = Settings()

engine = create_engine(settings.DB_URL)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()
    

def connect():
  try:
    Base.metadata.create_all(bind=engine)
  except Exception as e:
    print(e.__class__)
    print(e)
    exception_handler(e)


def get_db():
  try:
    db = SessionLocal()
    yield db
  except Exception as e:
    exception_handler(e)
  finally:
    db.close()