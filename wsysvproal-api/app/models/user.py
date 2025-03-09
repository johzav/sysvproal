from sqlalchemy import Column, Integer, String, Enum, TIMESTAMP
from app.db.session import Base
import enum

class UserStatus(enum.Enum):
    active = "active"
    inactive = "inactive"

class AppUsers(Base):
    __tablename__ = "App_Users"
    app_user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    status = Column(Enum(UserStatus), default=UserStatus.active)
    creation_date = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
