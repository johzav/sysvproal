from pydantic import BaseModel

class RoleCreate(BaseModel):
    role_name: str
    description: str

class RoleResponse(BaseModel):
    id: int
    role_name: str
    description: str
