from datetime import datetime
from typing import Optional
import uuid
from fastapi import Query
from fastapi_filter import FilterDepends
from sqlalchemy import desc, select
from sqlmodel import Session
from automapper import mapper
from construction_app.core.utils.pagination import paginate
from construction_app.models.models import Role, Users
from construction_app.schemas.user import CreateRoles, CreateUser, RolesFilter, UserList
from construction_app.schemas.user import UserListResponse, UserLogin  # Assuming you have a Users model

async def get_users(db: Session):
    print(f"print@1")
    query = select(Users.userid, Users.username, Users.phonenumber,
                   Users.email).where(Users.isactive == True)
    results = db.exec(query).all()
    # print(f"results{results}")
    if results:
        # mapping multi row data
        users_data = [mapper.to(UserListResponse).map(i_user) for i_user in results]
        # map singel row data
        # users_data =  mapper.to(schemas).map(results)
    return users_data



async def find_user_by_mail(db: Session, users: UserLogin) -> Optional[Users]:
    statement = select(Users).where(Users.email == users.email, Users.password == users.password)
    user = db.exec(statement).first()
    print(f"users in repo {user}")
    if not user:
        return 1
    user_data = mapper.to(UserList).map(user[0])
    
    return 1 if not user_data or user_data is None else user_data



async def get_roles_list(db: Session, page: int = Query(1, ge=1),
                             per_page: int = Query(100, ge=0),
                             role_filter: RolesFilter = FilterDepends(RolesFilter)):
    query = (select(Role.rolename, Role.description, 
                   Role.createddate, Role.roleid)
                .where(Role.isactive == True)
                .order_by(desc(Role.createddate)))
    filter_query = role_filter.filter(query)
    sort_by  = role_filter.sort(filter_query)
    return paginate(sort_by, page, per_page, db)


async def get_role_by_name(name: str, db: Session):

    query = (select(Role).where(Role.rolename == name))
    result = db.exec(query).first()
    return result



async def roles_create( data: CreateRoles, db: Session):
    
    old_role = await get_role_by_name(data.name, db)
    if old_role:
        return 1
    
    role_obj = mapper.to(Role).map(data)
    role_obj.roleid = uuid.uuid4()
    role_obj.isactive = True
    role_obj.createddate = datetime.now()
    role_obj.createdby = '58b8d829-945f-4c0c-a712-c37d68cd39d5'
    db.add(role_obj)
    db.commit()
    
    return role_obj


async def get_user_by_email(email: str, db: Session):

    query = (select(Users).where(Users.email == email))
    result = db.exec(query).first()
    return result



async def users_create( data: CreateUser, db: Session):
    
    old_user = await get_user_by_email(data.email, db)
    if old_user:
            return 1
    
    user_obj = mapper.to(Users).map(data)
    user_obj.userid = uuid.uuid4()
    user_obj.roleid = None
    user_obj.isactive = True
    user_obj.createddate = datetime.now()
    user_obj.createdby = '58b8d829-945f-4c0c-a712-c37d68cd39d5'
    db.add(user_obj)
    db.commit()
    
    return user_obj