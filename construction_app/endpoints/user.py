from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from construction_app.repos.user_repo import get_users
from construction_app.core.database.db import get_db
from construction_app.schemas.user import UserListResponse

router = APIRouter()

@router.get("/users", response_model=UserListResponse, tags=["Users"])
async def get_all_users(db: Session = Depends(get_db)):
    users = await get_users(db)
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No users found")
    json_compatible_users = jsonable_encoder(users)
    return {
        "status": "success",
        "message": "Users retrieved successfully",
        "data": UserListResponse(users=json_compatible_users)
    }