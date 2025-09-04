from click import group
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    age: int
    password: str

class Groups(BaseModel):
    name: str
    description : Optional[str] = None
    members: list[str]

class Expenses(BaseModel):
    group_id: str
    description: str
    amount: float
    paid_by: str
    split_between: list[str]


class Settlements(BaseModel):
    group_id: str
    from_user: str
    to_user: str
    amount: float


class Login(BaseModel):
    email: str
    password: str