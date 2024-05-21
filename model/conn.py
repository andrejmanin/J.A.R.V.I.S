from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('OPENAI_API_KEY')

if not API_KEY:
    raise ValueError('api not found')

client = OpenAI(
    api_key=API_KEY
)