from fastapi import FastAPI
from app.db.session import engine, Base
from app.api.endpoints.users import user_router

app = FastAPI()

# Crear tablas solo si no existen
def init_db():
    Base.metadata.create_all(bind=engine)  # No sobrescribe si ya existen

@app.on_event("startup")
def startup_event():
    init_db()

@app.get("/")
def read_root():
    return {"message": "API is running!"}