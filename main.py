from fastapi import FastAPI
from routes.user import user_router
from routes.groups import group_router
from routes.expenses import expense_router
from routes.settlements import settlements_router

app = FastAPI()
app.include_router(user_router)
app.include_router(group_router)
app.include_router(expense_router)
app.include_router(settlements_router)