from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from jose import jwt
from models import Users
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def encrypt_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def jwt_token(user: Users):
    payload = {
        "sub": str(user.id),
        "email": user.email
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
