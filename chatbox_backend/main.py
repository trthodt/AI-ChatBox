import os
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from app.routers import chatbox_router, auth_router
from app.core.database import connect
from app.models.user import User
from app.models.chatbox import ChatHistory, Chat

app = FastAPI()

origin = [
  'http://localhost:5173', 
  'http://localhost:3000', 
  'http://localhost:8000',
]
app.add_middleware(
  CORSMiddleware,
  allow_origins=origin,
  allow_credentials=True,
  allow_headers=['*'],
  allow_methods=['*'],
)

app.add_middleware(SessionMiddleware, secret_key=os.getenv('SESSION_SECRET_KEY'))

app.include_router(
  chatbox_router.router,
  prefix="/api"
)

app.include_router(
  auth_router.router,
  prefix="/api",
)

connect()

@app.get('/')
def home():
  return "initial server"
