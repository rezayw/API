from pydantic import BaseModel, EmailStr

# Untuk input saat register
class UserCreate(BaseModel):
    email: EmailStr
    full_name: str
    password: str

# Untuk output (tanpa password)
class UserOut(BaseModel):
    id: int
    email: EmailStr
    full_name: str

model_config = {
    "from_attributes": True
}

        
class UserLogin(BaseModel):
    email: EmailStr
    password: str

