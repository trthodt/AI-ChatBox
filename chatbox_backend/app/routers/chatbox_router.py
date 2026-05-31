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
    is_new_history, history_id = False, None
    if not chat_history:
      is_new_history = True
      
      history = chatbox.create_chat_history(user_id=current_user_id, chat_title=req.title, db=db)

      history_id = history.id
      chatbox.create_new_chat(history_id=history_id, is_user=True, chat_content=req.content, db=db)
    else:
      chatbox.create_new_chat(history_id=req.history_id, is_user=True, chat_content=req.content, db=db)

    res = chatbox.run_model(chat_content=req.content, db=db)

    if res:
      if is_new_history:
        chatbox.create_new_chat(history_id=history_id, is_user=False, chat_content=res, db=db)
      else:
        chatbox.create_new_chat(history_id=req.history_id, is_user=False, chat_content=res, db=db)
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
