from pydantic import BaseModel

class RegisterRequest(BaseModel):
  username: str
  password: str


class RegisterResponse(BaseModel):

  username: str
  created_at: str


class LoginRequest(BaseModel):

  username: str
  password: str

class LoginResponse(BaseModel):

  username: str
  login_at: str