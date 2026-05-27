from pydantic import BaseModel


class ChatBoxRequest(BaseModel):
  history_id: str
  title: str
  content: str

class ChatBoxResponse(BaseModel):
  text: str
