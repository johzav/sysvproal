from pydantic import BaseModel

class ModuleCreate(BaseModel):
    role_name: str
    description: str

class ModuleResponse(BaseModel):
    id: int
    role_name: str
    description: str
