from fastapi import APIRouter, Depends, Body
from starlette import status
from starlette.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from deps import get_user_service
from models import User
from user_service import UserService, CreateUserRequest

user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@user_router.get("/{user_id}", response_model=User)
async def get_user(*, user_service: UserService = Depends(get_user_service), user_id: int):
    user = await user_service.get(user_id)

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder(user))


@user_router.post("/", response_model=User)
async def create_user(*, user_service: UserService = Depends(get_user_service), user: CreateUserRequest = Body()):
    new_user = await user_service.create(user)

    return JSONResponse(status_code=status.HTTP_201_CREATED, content=jsonable_encoder(new_user))