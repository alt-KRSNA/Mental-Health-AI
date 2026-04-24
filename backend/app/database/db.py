from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from ..config import MONGO_URI, DB_NAME

client = None
db = None

try:
    # 🔹 Create MongoDB client
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)

    # 🔹 Test connection
    client.admin.command("ping")
    print("✅ MongoDB Connected Successfully!")

    # 🔹 Select database
    db = client[DB_NAME]

except ConnectionFailure as e:
    print("❌ MongoDB Connection Failed!")
    print(e)

except Exception as e:
    print("❌ Unexpected DB Error:", e)

__all__ = ["db", "client"]