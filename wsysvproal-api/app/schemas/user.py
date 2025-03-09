from pydantic import BaseModel, EmailStr
from enum import Enum

class UserStatus(str, Enum):
    active = "active"
    inactive = "inactive"

class UserCreate(BaseModel):
    username: str
    password: str
    email: EmailStr

class UserResponse(BaseModel):
    app_user_id: int
    username: str
    email: str
    status: UserStatus
