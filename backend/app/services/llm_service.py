from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_reply(message: str, emotion: str, context: list):

    # 🧠 Build conversation history
    history = ""
    for msg in context:
        history += f"User: {msg['message']}\nAI: {msg['reply']}\n"

    # 🎯 Better prompt (more natural)
    prompt = f"""
You are a warm, emotionally intelligent mental health assistant.

User Emotion: {emotion}

Conversation History:
{history}

User: {message}

Instructions:
- Be empathetic and understanding
- Talk like a real human, not a robot
- Keep response short (2-4 lines)
- Do NOT repeat the same sentence every time
- If user shares something emotional, acknowledge it first

Reply:
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a helpful and caring AI assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7  # 🔥 adds natural variation
        )

        reply = response.choices[0].message.content.strip()

        return reply if reply else "I'm here for you. Tell me more."

    except Exception as e:
        print("❌ LLM ERROR:", e)
        return "I'm here for you. Tell me more about how you're feeling."