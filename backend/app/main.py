from fastapi import FastAPI

app = FastAPI(title="StudySloth MVP")

@app.get('/')
async def root():
    return {"message": "Health OK"}