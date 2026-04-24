import os
from dotenv import load_dotenv
from pathlib import Path

# Load from the root project directory
env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path, verbose=True)

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")