import os 
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
NGROK_URL = os.getenv("NGROK_PUBLIC_URL")

INTERVIEW_DURATION = 15 * 60

TIME_WARNING = 5 * 60