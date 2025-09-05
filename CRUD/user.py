from bson import ObjectId
from auth import encrypt_password, jwt_token, verify_password

async def insert_user(user, db):
    user_dict = user.dict()
    user_dict["_id"] = str(ObjectId())
    user_dict["password"] = encrypt_password(user.password)
    user_dict["Role"] = "User"
    result = await db["Users"].insert_one(user_dict)
    new_user = await db["Users"].find_one({"_id": user_dict["_id"]})
    return jwt_token(new_user)

async def get_user_by_email(email: str, db):
    return await db["Users"].find_one({"email": email})

async def login_user(email: str, password: str, db):
    user = await get_user_by_email(email, db)
    if user and verify_password(password, user["password"]):
        return jwt_token(user)
    return None

async def admin_creator(user, db):
    user_dict = user.dict()
    user_dict["_id"] = str(ObjectId())
    user_dict["password"] = encrypt_password(user.password)
    user_dict["Role"] = "Admin"
    result = await db["Users"].insert_one(user_dict)
    new_user = await db["Users"].find_one({"_id": user_dict["_id"]})
    return jwt_token(new_user)