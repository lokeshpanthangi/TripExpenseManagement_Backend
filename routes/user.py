from fastapi import APIRouter,Depends
from CRUD.user_crud import create_user, login
from sqlalchemy.orm import Session
from database import get_db
from pydantic_schemas import User,Login
from models import Users


user_router = APIRouter()


@user_router.post("/create_user")
def register_user(user: User, db: Session = Depends(get_db)):
    return create_user(user, db)


@user_router.post("/login/")
def login_user(user: Login, db: Session = Depends(get_db)):
    return login(user, db)


@user_router.get("/get_all_users")
def get_all_users(db: Session = Depends(get_db)):
    return db.query(Users).all()
