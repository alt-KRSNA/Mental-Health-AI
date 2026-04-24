from .db import db
from datetime import datetime

# 🔥 Ensure DB is connected
if db is None:
    raise Exception("❌ Database not initialized. Check db.py")

collection = db["messages"]


def save_message(user_id: str, message: str, emotion: str, reply: str):
    """
    Save a message to the database.
    """

    data = {
        "user_id": user_id,
        "message": message,
        "emotion": emotion,
        "reply": reply,
        "timestamp": datetime.utcnow()
    }

    try:
        result = collection.insert_one(data)

        # 🔥 DEBUG (VERY IMPORTANT)
        print("✅ Message saved!")
        print("🆔 Inserted ID:", result.inserted_id)

    except Exception as e:
        print("❌ DB SAVE ERROR:", e)


def get_recent_messages(user_id: str, limit: int = 5):
    """
    Get recent messages for a user.
    Returns oldest → newest (LLM-friendly order)
    """

    try:
        messages = list(
            collection.find({"user_id": user_id})
            .sort("timestamp", -1)
            .limit(limit)
        )

        print(f"📦 Fetched {len(messages)} messages for user: {user_id}")

        # 🔥 Convert ObjectId → string (important for JSON safety)
        for msg in messages:
            msg["_id"] = str(msg["_id"])

        return list(reversed(messages))

    except Exception as e:
        print("❌ DB FETCH ERROR:", e)
        return []