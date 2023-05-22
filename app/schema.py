from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic.types import conint


class UserCreate(BaseModel):
    email:EmailStr
    password:str
    

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class UserOut(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    class Config:
        orm_mode=True


class PostBase(BaseModel):
    title:str
    content:str
    published: bool =True

class Post_create(PostBase):
    pass

class Post_response(PostBase):
    id:int
    created_at:datetime
    owner_id:int
    owner:UserOut
    class Config:
        orm_mode =True

class PostOut(BaseModel):
    Post:Post_response
    votes:int
    class Config:
        orm_mode=True

class Token(BaseModel):
    access_token:str
    token_type:str
    
class TokenData(BaseModel):
    id:Optional[str] = None


class Vote(BaseModel):
    post_id:int
    dir:conint(le=1)