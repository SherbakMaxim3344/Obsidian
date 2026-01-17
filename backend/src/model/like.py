from pydantic import BaseModel
from datetime import datetime

class LikeInDB(BaseModel):
    id: int 
    user_id: int
    entity_type: str
    entity_id: int
    created_at: datetime
    

