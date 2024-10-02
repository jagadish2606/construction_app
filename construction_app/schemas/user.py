# from uuid import UUID
import uuid
from sqlmodel import SQLModel
from pydantic import BaseModel
from datetime import datetime
from fastapi_filter.contrib.sqlalchemy import Filter
from typing import Optional, List
from construction_app.models.models import Roles as Role

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
    roleid:  Optional[uuid.UUID] = None
    createddate: datetime
    createdby: Optional[uuid.UUID] = None
    updateddate: datetime
    updatedby: Optional[uuid.UUID] = None
    isactive: bool
    
    
class RolesList(SQLModel):
    roleid: uuid.UUID
    name: str
    description: str
    createddate: Optional[datetime] = None
    


class RolesFilter(Filter):
    
    order_by: Optional[list[str]] = ['name', 'description']
    search: Optional[str] = None
    
    class Constants(Filter.Constants):
        model = Role
        Search_model_fields = ["name", 'description']
        
        
class CreateRoles(SQLModel):
    name: str
    description: str
    
    
class CreateUser(SQLModel):
    firstname: str
    lastname: str
    email: str
    password: str 
    
