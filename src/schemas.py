from datetime import datetime, date
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr


class ContactModel(BaseModel):
    phone_number: str = Field(max_length=20)


class ContactResponse(ContactModel):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    day_of_born: date
    email: EmailStr
    description: str = Field(max_length=300)


class UserModel(UserBase):
    contacts: List[int]


class UserResponse(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    contacts: List[ContactResponse]

    class Config:
        orm_mode = True

