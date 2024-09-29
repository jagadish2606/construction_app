from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session
from fastapi.encoders import jsonable_encoder
from fastapi_versioning import version
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from construction_app.repos.user_repo import find_user_by_mail, get_users
from construction_app.core.database.db import get_db
from construction_app.schemas.core import ResponseModel
from construction_app.schemas.user import UserListResponse, UserLogin

router = APIRouter()


@router.get("/list", status_code=200, tags=["Users"], description='all users list', response_model=ResponseModel)
@version(1)
async def get_all_users(db: Session = Depends(get_db)):
    users = await get_users(db)
    if users:
        response = ResponseModel(data=users)
        return JSONResponse(jsonable_encoder(response), status_code=HTTP_200_OK)
    
    response = ResponseModel(status=401, message='Users not found')
    return JSONResponse(jsonable_encoder(response), status_code=HTTP_404_NOT_FOUND)

@router.post("/login", tags=["Users"], description="user login ")    
@version(1)
async def login(user: UserLogin, db: Session = Depends(get_db)):
    print(f"user{user}")
    user_found = await find_user_by_mail(db, user)       
    if user_found == 1: 
        response = ResponseModel(status=401, message='User not found')
        return JSONResponse(jsonable_encoder(response), status_code=HTTP_404_NOT_FOUND)
    response = ResponseModel( data=user_found, status=200, message='User login sucesufully')
    return JSONResponse(jsonable_encoder(response), status_code=HTTP_200_OK)