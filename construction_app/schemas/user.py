from typing import List, Optional
from pydantic import BaseModel

class UserResponse(BaseModel):
    id: str
    name: str
    email: str

    class Config:
        orm_mode = True

class UserListResponse(BaseModel):
    users: List[UserResponse]
