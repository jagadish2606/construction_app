from fastapi import APIRouter, Depends
from construction_app.schemas.user import UserCreate

router = APIRouter()

@router.post("/users/")
def create_user(user: UserCreate):
    return {"user": user}
