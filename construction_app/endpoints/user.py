from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_filter import FilterDepends
from sqlmodel import Session
from fastapi.encoders import jsonable_encoder
from fastapi_versioning import version
from starlette.responses import JSONResponse
from starlette.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT
from construction_app.core.database.db import get_db
from construction_app.core.utils.pagination import PaginatedParams
from construction_app.core.utils.pagination.schemas import PaginatedResponse
from construction_app.schemas.core import ResponseModel
from construction_app.schemas.user import CreateRoles, CreateUser, RolesFilter, RolesList, UserListResponse, UserLogin
from construction_app.repos.user_repo import find_user_by_mail, get_roles_list, get_users, roles_create, users_create

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



@router.get("/roles/list", status_code=200, tags=["Roles"],
            description="All employee roles paginated list", response_model=PaginatedResponse[RolesList])
@version(1)
async def employee_all(db: Session = Depends(get_db),
                       params: PaginatedParams = Depends(),
                       employee_filter: RolesFilter = FilterDepends(RolesFilter)):
     return await get_roles_list(db, params.page, params.per_page, employee_filter)
 

@router.post("role/add", status_code=200, tags=["Roles"],
             description="Roles add API", response_model=ResponseModel)
@version(1)
async def add_roles(data: CreateRoles, db: Session = Depends(get_db)):
    role_obj = await roles_create(data, db)
    if role_obj:
        if role_obj == 1:
            response = ResponseModel(status=409, message='Roles alreay exist')
            return JSONResponse(jsonable_encoder(response), status_code=HTTP_409_CONFLICT) 
            
        response = ResponseModel(data=role_obj)
        return JSONResponse(jsonable_encoder(response), status_code=HTTP_200_OK)
    
    response = ResponseModel(status=401, message='Users not found')
    return JSONResponse(jsonable_encoder(response), status_code=HTTP_404_NOT_FOUND) 


@router.post("/add", status_code=200, tags=["Roles"],
             description="add new user API", response_model=ResponseModel)
@version(1)
async def add_users(data: CreateUser, db: Session = Depends(get_db)):
    user_obj = await users_create(data, db)
    if user_obj:
        if user_obj == 1:
            response = ResponseModel(status=409, message='Roles alreay exist')
            return JSONResponse(jsonable_encoder(response), status_code=HTTP_409_CONFLICT) 
            
        response = ResponseModel(data=user_obj)
        return JSONResponse(jsonable_encoder(response), status_code=HTTP_200_OK)
    
    response = ResponseModel(status=401, message='Users not found')
    return JSONResponse(jsonable_encoder(response), status_code=HTTP_404_NOT_FOUND) 
