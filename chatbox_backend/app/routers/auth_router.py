from fastapi import APIRouter, Depends, Request, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.utils.exception_handle import exception_handler
from app.services.auth_service import AuthService
from app.schemas.user import RegisterRequest, RegisterResponse, LoginRequest, LoginResponse

router = APIRouter(
  prefix="/auth"
)

@router.post('/register')
def register(req: RegisterRequest, db: Session = Depends(get_db)) ->  RegisterResponse:
  try:
    auth_service = AuthService()
    response = auth_service.register(req, db=db)
    return response
  except Exception as e:
    raise exception_handler(e)
  

@router.post('/login')
def login(request: Request, req: LoginRequest, db: Session = Depends(get_db)) ->  LoginResponse:
  try:
    auth_service = AuthService()
    response = auth_service.login(request, req, db=db)

    return response
  except Exception as e:
    raise exception_handler(e)
  
@router.get('/is-login')
def check_login(request: Request):
  user_id = request.session.get('user_id')
  if not user_id:
    raise HTTPException(
      status_code=status.HTTP_401_UNAUTHORIZED,
      detail={'success': False, 'message': 'unauthorized'}
    )
  return user_id