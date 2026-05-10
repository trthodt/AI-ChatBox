from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.utils.exception_handle import exception_handler
from app.services.chatbox_service import ChatboxService
from app.schemas.chatbox import ChatBoxRequest, ChatBoxResponse

router = APIRouter(
  prefix="/chatbox"
)

@router.post('/chat')
def chat(req: ChatBoxRequest, db: Session = Depends(get_db)) ->  ChatBoxResponse:
  try:
    chatbox = ChatboxService()
    res = chatbox.run_model(chat_content=req.content, db=db)
    if res:
      return ChatBoxResponse(
        text=res
      )
    else:
      raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail={"Run model failed"}
      )
  except Exception as e:
    exception_handler(e)