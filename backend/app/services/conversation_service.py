from .emotion_service import detect_emotion
from .llm_service import generate_reply
from ..database.crud import save_message, get_recent_messages


def process_chat(user_id: str, message: str):
    """
    Process a chat message and generate a response.

    Flow:
    message → emotion → memory → LLM → save → return
    """

    # Step 1: Detect Emotion
    emotion = detect_emotion(message)

    # Step 2: Fetch Memory (Fix order: oldest → newest)
    past = list(reversed(get_recent_messages(user_id)))

    # Step 3: Generate Reply (Safe execution)
    try:
        reply = generate_reply(message, emotion, past)
    except Exception as e:
        print("LLM ERROR:", e)
        reply = "I'm here for you. Tell me more about what's on your mind."

    # Step 4: Save to DB
    save_message(user_id, message, emotion, reply)

    # Debug logs (very useful)
    print(f"[USER]: {message}")
    print(f"[EMOTION]: {emotion}")
    print(f"[AI]: {reply}")

    return reply, emotion


__all__ = ["process_chat"]