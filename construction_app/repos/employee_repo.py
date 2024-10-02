from datetime import datetime
import uuid
from fastapi import Query
from fastapi_filter import FilterDepends
from sqlalchemy import desc, select
from sqlmodel import Session
from automapper import mapper
from construction_app.core.utils.pagination import paginate
from construction_app.models.models import Employees
from construction_app.schemas.employee import CreateEmployee, EmployeeFilter


async def get_employees_list(db: Session, page: int = Query(1, ge=1),
                             per_page: int = Query(100, ge=0),
                             employee_filter: EmployeeFilter = FilterDepends(EmployeeFilter)):
    # query = (select(Employees).where(Employees.isactive == True)
                # .order_by(desc(Employees.createddate)))
    query = (select(Employees.firstname, Employees.lastname, Employees.email, 
                   Employees.employeeid, Employees.phonenumber, Employees.isactive,
                   Employees.userid, Employees.position)
                .where(Employees.isactive == True)
                .order_by(desc(Employees.createddate)))
    filter_query = employee_filter.filter(query)
    sort_by  = employee_filter.sort(filter_query)
    return paginate(sort_by, page, per_page, db)



async def get_employee_by_id(mail: str, db: Session):

    query = (select(Employees).where(Employees.email == mail))
    result = db.exec(query).first()
    return result



async def employee_create( data: CreateEmployee, db: Session):
    
    old_employee = await get_employee_by_id(data.email, db)
    if old_employee:
        return 1
    
    employee_obj = mapper.to(Employees).map(data)
    employee_obj.employeeid = uuid.uuid4()
    employee_obj.isactive = True
    employee_obj.createddate = datetime.datetime.now()
    employee_obj.createdby = '58b8d829-945f-4c0c-a712-c37d68cd39d5'
    db.add(employee_obj)
    db.commit()
    
    return employee_obj
    
    
    