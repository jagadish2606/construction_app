from datetime import datetime
from decimal import Decimal
import uuid
from fastapi_filter.contrib.sqlalchemy import Filter
from typing import Optional

from sqlmodel import SQLModel
from construction_app.models.models import Employee as Emp



class EmployeeList(SQLModel):
    employeeid: uuid.UUID
    fullname: str
    designation: str
    email: Optional[str] = None
    phonenumber: Optional[str] = None
    # position: Optional[str] = None
    # salary: Optional[Decimal] = None
    # advancegetamount: Optional[Decimal] = None
    userid: Optional[uuid.UUID] = None
    createddate: Optional[datetime] = None
    createdby:  Optional[uuid.UUID] = None
    updateddate: Optional[datetime] = None
    updatedby:  Optional[uuid.UUID] = None
    isactive: bool


class EmployeeFilter(Filter):
    
    order_by: Optional[list[str]] = ['fullname', 'createddate']
    search: Optional[str] = None
    
    class Constants(Filter.Constants):
        model = Emp
        Search_model_fields = ["email", 'fullname', 'designation']
        
        
class CreateEmployee(SQLModel):
    fullname: str
    email: Optional[str] = None
    phonenumber: Optional[str] = None
    designation: Optional[str] = None
    joineddate: Optional[datetime] = None
    advancegetamount: Optional[Decimal] = None
    userid: Optional[uuid.UUID] = None
    
    
class EditEmployee(SQLModel):
    employeeid: uuid.UUID
    fullname: str
    email: Optional[str] = None
    phonenumber: Optional[str] = None
    designation: Optional[str] = None
    joineddate: Optional[datetime] = None
    advancegetamount: Optional[Decimal] = None
    userid: Optional[uuid.UUID] = None
    