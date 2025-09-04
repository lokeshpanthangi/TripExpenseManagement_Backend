from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def encrypt_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

def jwt_token(user: dict):
    payload = {
        "_id": str(user["_id"]),
        "email": user["email"]
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return "Invalid token"
    
security = HTTPBearer()


def validate(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    tokendata = decode_token(token)
    if tokendata == "Invalid token":
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return tokendata