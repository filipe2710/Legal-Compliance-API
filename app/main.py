from fastapi import FastAPI
from .core import settings

from .routers import users

app = FastAPI(
  title=settings.PROJECT_NAME,
  version=settings.PROJECT_VERSION,
  description=settings.PROJECT_DESCRIPTION
)

app.include_router(users.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}