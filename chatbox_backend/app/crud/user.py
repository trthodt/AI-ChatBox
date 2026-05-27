from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import RegisterRequest
from passlib.context import CryptContext

class UserRepository():

  password_context: CryptContext

  def __init__(self):
    self.password_context = CryptContext(schemes='bcrypt', deprecated='auto')

  def get_user_by_username(self, username: str, db: Session) -> User:

    user = db.query(User).filter(User.username==username).first()
    return user

  def create_user(self, req: RegisterRequest, db: Session) -> User:

    hashed_pass = self.password_context.hash(req.password)
    user = User(
      username=req.username,
      password=hashed_pass,
      is_deleted=False,
    )

    db.add(user)
    db.commit()
    return user
