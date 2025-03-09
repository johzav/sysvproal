from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Roles(Base):
    __tablename__ = "Roles"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    role_name = Column(String(50), unique=True, nullable=False)
    description = Column(String(255))
