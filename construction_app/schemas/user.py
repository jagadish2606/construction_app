from uuid import UUID
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class UserResponse(BaseModel):
    userid: UUID
    firstname: str
    lastname: str
    email: str
    # password: str  # Consider excluding sensitive data like password
    # roleid: Optional[UUID]
    # createddate: Optional[datetime]
    # createdby: Optional[UUID]
    # updateddate: Optional[datetime]
    # updatedby: Optional[UUID]
    # isactive: Optional[bool]

    class Config:
        orm_mode = True  # Allows the model to work with ORM objects

# Example of a list response
class UserListResponse(BaseModel):
    users: List[UserResponse]  # Use List for type hinting
