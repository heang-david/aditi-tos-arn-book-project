from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY:   str = "changeme"
    ALGORITHM:    str = "HS256"
    DEBUG:        bool = False

    # Admin JWT token expires in 10 minutes
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10

    class Config:
        env_file = ".env"

settings = Settings()