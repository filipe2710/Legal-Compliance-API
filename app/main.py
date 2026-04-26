from fastapi import FastAPI
from .core import settings

app = FastAPI(
  title=settings.PROJECT_NAME,
  version=settings.PROJECT_VERSION,
  description=settings.PROJECT_DESCRIPTION
)

@app.get("/")
def read_root():
    return {"Hello": "World"}