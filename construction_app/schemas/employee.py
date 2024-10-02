from datetime import datetime
from decimal import Decimal
import uuid
from fastapi_filter.contrib.sqlalchemy import Filter
from typing import Optional

from sqlmodel import SQLModel
from construction_app.models.models import Employees as Emp



class EmployeeList(SQLModel):
    employeeid: uuid.UUID
    firstname: str
    lastname: str
    email: Optional[str] = None
    phonenumber: Optional[str] = None
    position: Optional[str] = None
    salary: Optional[Decimal] = None
    advancegetamount: Optional[Decimal] = None
    userid: Optional[uuid.UUID] = None
    createddate: Optional[datetime] = None
    createdby:  Optional[uuid.UUID] = None
    updateddate: Optional[datetime] = None
    updatedby:  Optional[uuid.UUID] = None
    isactive: bool


class EmployeeFilter(Filter):
    
    order_by: Optional[list[str]] = ['firstname', 'lastname']
    search: Optional[str] = None
    
    class Constants(Filter.Constants):
        model = Emp
        Search_model_fields = ["email", 'firstname', 'lastname']
        
        
class CreateEmployee(SQLModel):
    firstname: str
    lastname: str
    email: Optional[str] = None
    phonenumber: Optional[str] = None
    position: Optional[str] = None
    salary: Optional[Decimal] = None
    advancegetamount: Optional[Decimal] = None
    userid: Optional[uuid.UUID] = None
    