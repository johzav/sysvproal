from sqlalchemy.orm import Session
from app.models.user import AppUsers
from app.schemas.user import UserCreate
from app.core.security import hash_password

def create_user(db: Session, user: UserCreate):
    db_user = AppUsers(username=user.username, password=hash_password(user.password), email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
