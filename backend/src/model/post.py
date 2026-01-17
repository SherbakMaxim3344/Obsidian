from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime



class PostBase(BaseModel): 
    title: str
    content: str
    
class PostCreate(PostBase):
    @field_validator('title')
    @classmethod
    def validate_title(cls, v: str) -> str:
        if len(v) < 1:
            raise ValueError('Title must be at least 1 character')
        return v
    
class PostInDB(PostBase):
    id:  int
    author_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    like_count: int = 0 
    comment_count: int = 0
    channel_id: Optional[int] = None