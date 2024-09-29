from typing import Optional
from sqlalchemy import select
from sqlmodel import Session
from automapper import mapper
from construction_app.models.models import Users
from construction_app.schemas.user import UserList, UserListResponse, UserLogin  # Assuming you have a Users model

async def get_users(db: Session):
    # print(f"print@1")
    query = select(Users.userid, Users.firstname, Users.lastname,
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
    statement = select(Users).where(Users.email == users.username, Users.password == users.password)
    user = db.exec(statement).first()
    print(f"users in repo {user}")
    if not user:
        return 1
    user_data = mapper.to(UserList).map(user[0])
    
    return 1 if not user_data or user_data is None else user_data
