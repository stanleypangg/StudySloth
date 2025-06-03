from pydantic import BaseModel

class Settings(BaseModel):
    database_url: str
    jwt_secret: str
    jwt_algorithm: str
    
    class Config:
        env_file = '.env'

settings = Settings()