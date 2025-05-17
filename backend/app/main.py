from fastapi import FastAPI
from api import upload

app = FastAPI(title="StudySloth MVP")
app.include_router(upload.router)

@app.get('/')
async def root():
    return {"message": "Health OK"}