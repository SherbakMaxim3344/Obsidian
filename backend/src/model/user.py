from pydantic import BaseModel, Field, field_validator, EmailStr
from typing import Optional
from datetime import datetime, timezone
import re

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    
    @field_validator('username')
    @classmethod
    def validate_username(cls, v:str)->str:
        if len(v)<3:
            raise ValueError('Username must be at least 3 characters')
        if not re.match(r'^[a-zA-Z0-9_]+$', v):
            raise ValueError('Username can only contain letters, numbers and underscore')
        return v
    
    @field_validator('password')
    @classmethod
    def validate_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        return v

class UserInDB(UserBase):
    id: Optional[int] = None
    password_hash: str
    avatar_url: Optional[str] = None
    bio: Optional[str] = None
    created_at: Optional[datetime] = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: Optional[datetime] = None
    last_login: Optional[datetime] = None
    is_active: bool = True
    is_verified: bool = False
    

class UserPublic(UserBase):
    id: int
    avatar_url: Optional[str] = None
    bio: Optional[str] = None
    created_at: datetime
    is_verified: bool = False