from sqlalchemy import select
from sqlmodel import Session
from construction_app.models.models import Users  # Assuming you have a Users model

async def get_users(db: Session):
    print(f"print@1")
    query = select(Users.userid, Users.firstname, Users.lastname,
                   Users.email).where(Users.isactive == True)
    results = db.exec(query).all()
    print(f"results{results}")
    return results
