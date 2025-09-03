from fastapi import FastAPI
from models import Base
from database import engine
from routes.user import user_router

Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(user_router)