from pydantic import BaseModel


class ChatBoxRequest(BaseModel):
  content: str

class ChatBoxResponse(BaseModel):
  text: str
