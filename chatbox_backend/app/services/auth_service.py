from fastapi import HTTPException, status, Request
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from app.schemas.user import RegisterRequest, RegisterResponse, LoginRequest, LoginResponse
from app.crud.user import UserRepository

class AuthService():

  user_repository: UserRepository

  def __init__(self):
    self.user_repository = UserRepository()

  def register(self, req: RegisterRequest, db: Session) -> RegisterResponse:
    existed_user = self.user_repository.get_user_by_username(req.username, db)
    
    if existed_user:
      raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail={'success': False, 'message': 'Username is already registered'},
      )
    
    user = self.user_repository.create_user(req, db)
    
    return RegisterResponse(
      username=user.username,
      created_at=user.created_at,
    )
  
  def login(self, request: Request, req: LoginRequest, db: Session) -> LoginResponse:
    existed_user = self.user_repository.get_user_by_username(req.username, db)
    
    if not existed_user:
      raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={'success': False, 'message': 'Username or password is not correct'},
      )
    
    is_pass_match = self.user_repository.password_context.verify(req.password, existed_user.password)
    
    if not is_pass_match:
      raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={'success': False, 'message': 'Username or password is not correct'},
      )
    
    request.session['user_id'] = existed_user.id
    # set server-checkable expiry (1 hour)
    request.session['expires_at'] = int(datetime.now(timezone.utc).timestamp()) + 3600
    return LoginResponse(
      username=existed_user.username,
      login_at=str(int(datetime.now(timezone.utc).timestamp())),
    )