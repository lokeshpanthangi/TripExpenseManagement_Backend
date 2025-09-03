from uuid import uuid4
from models import Users
from auth import verify_password, encrypt_password, jwt_token
from pydantic_schemas import User,Login

 

def create_user(user: User, db):
    db_user = Users(
        id=uuid4(),
        name=user.name,
        email=user.email,
        age=user.age,
        password=encrypt_password(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return jwt_token(db_user)


def login(user: Login, db):
    db_user = db.query(Users).filter(Users.email == user.email).first()
    if not db_user or not verify_password(user.password, db_user.password):
        return {"error": "Invalid email or password"}
    return jwt_token(db_user)

