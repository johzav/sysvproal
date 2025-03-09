import os
from pydantic import BaseSettings

DATABASE_URL = os.getenv("DATABASE_URL", "mysql+pymysql://user:password@localhost:3306/mydatabase")

class Settings(BaseSettings):
    DATABASE_URL: str = "mysql+pymysql://user:password@localhost/db_name"
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")

    class Config:
        env_file = ".env"

settings = Settings()