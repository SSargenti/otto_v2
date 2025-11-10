from fastapi import FastAPI
from app.routers.generate import router as generate_router

app = FastAPI(title="Otto v2 - Gerador de Laudos", version="2.0.0")
app.include_router(generate_router)