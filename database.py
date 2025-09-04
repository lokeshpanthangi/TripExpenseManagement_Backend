from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os


load_dotenv()


####... Production setup...####
#from contextlib import asynccontextmanager
# async def startup_db_client(app):
#     app.mongodb_client = AsyncIOMotorClient(
#         os.getenv("MONGO_URL"))
#     app.mongodb = app.mongodb_client.get_database(os.getenv("DATABASE_NAME"))
#     print("MongoDB connected.")


# async def shutdown_db_client(app):
#     app.mongodb_client.close()
#     print("Database disconnected.")


# @asynccontextmanager
# async def lifespan(app):
#     # Start the database connection
#     await startup_db_client(app)
#     yield
#     # Close the database connection
#     await shutdown_db_client(app)

####... Development setup...####

client = AsyncIOMotorClient(os.getenv("MONGO_URL"))
db = client.get_database(os.getenv("DATABASE_NAME"))