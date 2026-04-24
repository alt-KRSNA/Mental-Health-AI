from fastapi import FastAPI
from app.routes import chat   # 👈 THIS LINE

app = FastAPI()

app.include_router(chat.router)   # 👈 THIS LINE

@app.get("/")
def home():
    return {"message": "Mental Health AI Backend Running"}