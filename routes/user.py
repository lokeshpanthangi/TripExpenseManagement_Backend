from fastapi import APIRouter, HTTPException
from CRUD.user import insert_user, get_user_by_email, login_user
from pydantic_schemas import User, Login
from database import db

user_router = APIRouter()


@user_router.post("/create_user")
async def create_user_route(user: User):
    token = await insert_user(user, db)
    return {"access_token": token, "token_type": "bearer"}

@user_router.get("/get_user/{email}")
async def get_user_route(email: str):
    user = await get_user_by_email(email, db)
    if user:
        user.pop("password")
    return {"user": user}

@user_router.post("/login")
async def login_route(login: Login):
    token = await login_user(login.email, login.password, db)
    if token:
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")