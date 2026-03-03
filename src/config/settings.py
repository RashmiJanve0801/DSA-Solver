import os
from dotenv import load_dotenv

from autogen_ext.models.openai import OpenAIChatCompletionClient
from src.config.constant import MODEL, API_KEY

load_dotenv()
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

def get_model_client():
    model_client = OpenAIChatCompletionClient(model=MODEL, api_key=os.getenv("GOOGLE_API_KEY"))
    return model_client