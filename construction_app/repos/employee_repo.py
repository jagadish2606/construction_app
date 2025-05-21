from datetime import datetime
import uuid
from fastapi import Query
from fastapi_filter import FilterDepends
from sqlalchemy import desc, select
from sqlmodel import Session
from automapper import mapper
from construction_app.core.utils.pagination import paginate
from construction_app.models.models import Employee
from construction_app.schemas.employee import CreateEmployee, EditEmployee, EmployeeFilter


async def get_employees_list(db: Session, page: int = Query(1, ge=1),
                             per_page: int = Query(100, ge=0),
                             employee_filter: EmployeeFilter = FilterDepends(EmployeeFilter)):
    # query = (select(Employee).where(Employee.isactive == True)
                # .order_by(desc(Employee.createddate)))
    query = (select(Employee.fullname, Employee.joineddate, Employee.email, 
                   Employee.employeeid, Employee.phonenumber, Employee.isactive,
                   Employee.userid, Employee.designation)
                .where(Employee.isactive == True)
                .order_by(desc(Employee.createddate)))
    filter_query = employee_filter.filter(query)
    sort_by  = employee_filter.sort(filter_query)
    return paginate(sort_by, page, per_page, db)



async def get_employee_by_mail(mail: str, db: Session):

    query = (select(Employee).where(Employee.email == mail))
    result = db.exec(query).first()
    return result



async def get_employee_by_id(employee_id: str, db: Session):

    query = (select(Employee).where(Employee.employeeid == employee_id))
    result = db.exec(query).first()
    return result



async def employee_create( data: CreateEmployee, db: Session):
    
    old_employee = await get_employee_by_mail(data.email, db)
    if old_employee:
        return 1
    
    employee_obj = mapper.to(Employee).map(data)
    employee_obj.employeeid = uuid.uuid4()
    employee_obj.isactive = True
    employee_obj.createddate = datetime.now()
    employee_obj.createdby = '58b8d829-945f-4c0c-a712-c37d68cd39d5'
    db.add(employee_obj)
    db.commit()
    
    return employee_obj




async def employee_edit(data: EditEmployee, db: Session):
    # Fetch existing employee by ID
    employee_obj = await get_employee_by_id(data.employeeid, db)
    if not employee_obj:
        return 1  # Or raise an exception

    # Update all fields dynamically (excluding employeeid)
    for field, value in data.__dict__.items():
        if field != "employeeid" and value is not None:
            setattr(employee_obj, field, value)

    # Set metadata fields
    employee_obj.updateddate = datetime.now()
    employee_obj.updatedby = '58b8d829-945f-4c0c-a712-c37d68cd39d5'  # Ideally from current session/user

    # Commit and refresh
    db.commit()
    db.refresh(employee_obj)

    return employee_obj
    
    
    