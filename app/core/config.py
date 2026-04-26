from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  PROJECT_NAME: str = "Legal Compliance API"
  PROJECT_VERSION: str = "0.1.0"
  PROJECT_DESCRIPTION: str = "API for simulating legal validation, LGPD compliance, and consent registration."
  
  DEBUG: bool = True
  
  DATABASE_URL: str = "sqlite:///./Legal_Compliance.db"
  
  class Config:
    env_file = ".env"
  
settings = Settings()