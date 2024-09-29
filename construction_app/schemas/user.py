# from uuid import UUID
import uuid
from sqlmodel import SQLModel
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class UserListResponse(SQLModel):
    userid: uuid.UUID
    firstname: str
    lastname: str
    email: str
    
class UserLogin(SQLModel):
    username: str 
    password: str
    
    
class UserList(SQLModel):
    userid: uuid.UUID
    firstname: str
    lastname: str
    email: str
    roleid: uuid.UUID
    createddate: datetime
    createdby: Optional[uuid.UUID] = None
    updateddate: datetime
    updatedby: Optional[uuid.UUID] = None
    isactive: bool
    
