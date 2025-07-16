import os
from dotenv import load_dotenv

from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constant import MODEL

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
API_KEY = os.getenv("GOOGLE_API_KEY")

def get_model_client():
    model_client = OpenAIChatCompletionClient(model=MODEL, api_key=API_KEY)
    return model_client
