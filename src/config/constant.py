import os

MODEL = 'gemini-2.5-flash'
TEXT_MENTION = 'STOP'
WORK_DIR = 'temp'
TIMEOUT = 1000
MAX_TURNS = 25
API_KEY = os.getenv("GOOGLE_API_KEY")