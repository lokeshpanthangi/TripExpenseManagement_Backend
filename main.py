from fastapi import FastAPI
from routes.user import user_router
from routes.groups import group_router

app = FastAPI()
app.include_router(user_router)
app.include_router(group_router)