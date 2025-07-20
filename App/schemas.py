from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class JobCreate(BaseModel):
    title: str
    description: str

class ShowJob(BaseModel):
    id: int
    title: str
    description: str

    model_config = {
        "from_attributes": True
    }