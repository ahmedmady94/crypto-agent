import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
FREECRYPTO_TOKEN = os.getenv("FREE_CRYPTO_API")
NEWSAPI_KEY = os.getenv("NEWS_API")

llm = ChatOpenAI(model="gpt-4")
