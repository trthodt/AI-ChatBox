import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from app.routers import chatbox_router, auth_router
from app.core.database import connect
from app.models.user import User
from app.models.chatbox import ChatHistory, Chat
from datetime import datetime, timezone
from starlette.responses import JSONResponse

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

app.add_middleware(
  SessionMiddleware,
  secret_key=os.getenv('SESSION_SECRET_KEY'),
  max_age=3600,  # session cookie expires in 1 hour
  same_site='lax',
  https_only=True,
)


@app.middleware("http")
async def enforce_session_expiry(request: Request, call_next):
  # Only check expiry when SessionMiddleware has attached a session
  if 'session' in request.scope:
    expires_at = request.session.get('expires_at')
    if expires_at:
      try:
        if datetime.now(timezone.utc).timestamp() > int(expires_at):
          request.session.clear()
          return JSONResponse(status_code=401, content={'success': False, 'message': 'Session expired'})
      except Exception:
        request.session.clear()
        return JSONResponse(status_code=401, content={'success': False, 'message': 'Session invalid'})
  return await call_next(request)

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
