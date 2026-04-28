from fastapi import APIRouter, HTTPException
from ..models.chat_model import ChatRequest, ChatResponse
from ..services.conversation_service import process_chat

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):
    """Handle chat requests and return AI responses."""

    # 🔹 Basic validation
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    print(f"[REQUEST] {request.user_id}: {request.message}")

    try:
        reply, emotion = process_chat(
            request.user_id,
            request.message
        )

        return ChatResponse(
            reply=reply,
            emotion=emotion
        )

    except Exception as e:
        print("API ERROR:", e)
        raise HTTPException(status_code=500, detail="Internal Server Error")


__all__ = ["router"]