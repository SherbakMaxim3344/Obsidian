from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime

class CommentBase(BaseModel):
    content: str
    

class CommentCreate(CommentBase):
    @field_validator('content')
    @classmethod
    def validate_content(cls, v: str) -> str:
        if len(v) < 1:
            raise ValueError('content must be at least 1 character')
        return v
    



class CommentInDB(CommentBase):
    id: int
    post_id: int
    author_id: int
    created_at: datetime
    channel_id: Optional[int] = None
    