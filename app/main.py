from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Crypto LangGraph Agent")

app.include_router(router)
