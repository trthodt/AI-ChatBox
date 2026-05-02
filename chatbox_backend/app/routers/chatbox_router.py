from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db

router = APIRouter(
  prefix="/chatbox"
)

@router.post('/chat')
def chat(db: Session = Depends(get_db)):
  pass