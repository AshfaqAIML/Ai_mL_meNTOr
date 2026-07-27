import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Vercel uses /tmp for writable storage (ephemeral, resets on cold start)
# Railway and local use the project's data/ directory
VERCEL = os.getenv("VERCEL") == "1"

if VERCEL:
    DATA_DIR = Path("/tmp/mlmentor_data")
else:
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_DIR = BASE_DIR / "data"

USERS_DIR = DATA_DIR / "users"
USERS_DIR.mkdir(parents=True, exist_ok=True)

LLM_API_KEY = os.getenv("LLM_API_KEY", "")
LLM_API_URL = os.getenv("LLM_API_URL", "")
MODEL_NAME = os.getenv("MODEL_NAME", "default-model")
