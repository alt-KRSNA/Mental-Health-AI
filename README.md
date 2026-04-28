## Mental Health AI 

# Mental Health AI Assistant

An AI-powered mental health assistant that interacts with users, detects emotions, and responds with empathetic, human-like conversations.

---

##  Features

- Chat-based interaction (like a friend)
- Emotion detection (text-based)
- AI-powered responses using Groq (LLaMA 3)
- Conversation memory (MongoDB)
- Multi-device access (via network / deployment)
- Fast and responsive UI (Streamlit)

---

## Tech Stack

- **Frontend:** Streamlit  
- **Backend:** FastAPI  
- **Database:** MongoDB Atlas  
- **LLM:** Groq API (LLaMA 3)  
- **Containerization:** Docker  

---

## Project Structure


Mental Health Assistant/
│
├── backend/
│ ├── app/
│ ├── Dockerfile
│ └── requirements.txt
│
├── frontend/
│ ├── app.py
│ └── Dockerfile
│
├── docker-compose.yml
├── README.md
└── .gitignore


---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/mental-health-ai.git
cd mental-health-ai
2. Create Environment File

backend/.env

MONGO_URI=your_mongodb_uri
DB_NAME=mental_health_ai
GROQ_API_KEY=your_api_key
3. Run with Docker
docker-compose up --build
4. Open App
http://localhost:8501
Access on Other Devices

Find your IP:

ipconfig

Then open:

http://YOUR_IP:8501
How It Works
User sends message
Emotion is detected
Past messages are retrieved (memory)
LLM generates response
Conversation is stored in database
 Security Notes
.env file is ignored (not uploaded)
API keys are kept private
Future Improvements
Voice input/output
Emotion tracking dashboard
Advanced NLP emotion model
Full cloud deployment
BY
 Krishna


---

#  AFTER THIS

---

## STEP 1: Save file

`README.md`

---

## STEP 2: Add & push

```bash
git add README.md
git commit -m "Added README"
git push