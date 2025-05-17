from fastapi import APIRouter, UploadFile

router = APIRouter(
    prefix='/upload',
    tags=['upload']
)

@router.post('/')
async def upload():
    return 420