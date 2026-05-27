from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.utils.exception_handle import exception_handler
from app.services.chatbox_service import ChatboxService
from app.schemas.chatbox import ChatBoxRequest, ChatBoxResponse

router = APIRouter(
  prefix="/chatbox"
)

@router.post('/chat')
def chat(request: Request, req: ChatBoxRequest, db: Session = Depends(get_db)) ->  ChatBoxResponse:
  try:
    # check login session
    current_user_id = request.session.get('user_id')
    if not current_user_id:
      raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={'success': False, 'message': 'Unauthorized'}
      )
    
    chatbox = ChatboxService()

    chat_history = chatbox.get_history_by_id(history_id=req.history_id, user_id=current_user_id, db=db)
    
    if not chat_history:

      history = chatbox.create_chat_history(user_id=current_user_id, chat_title=req.title, db=db)

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
    raise exception_handler(e)
