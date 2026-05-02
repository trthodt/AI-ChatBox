from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.routers import chatbox_router
from app.core.database import connect
from app.schemas.user import User

app = FastAPI()

origin = [
  'http://localhost:5173/*', 
  'http://localhost:3000/*', 
  'http://localhost:8000/*'
]
app.add_middleware(
  CORSMiddleware,
  allow_origins=origin,
  allow_credentials=True,
  allow_headers=['*'],
  allow_methods=['*'],
)

app.include_router(
  chatbox_router.router,
  prefix="/api"
)

connect()

@app.get('/')
def home():
  return "initial server"
