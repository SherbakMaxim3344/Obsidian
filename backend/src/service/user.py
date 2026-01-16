from src.model.user import UserPublic, UserCreate, UserInDB
import src.data.user as data
from errors import Missing, Duplicate
from datetime import datetime, timezone
from .auth import get_password_hash

def get_all() -> list[UserPublic]:
    """UserPublic(**user.model_dump()) создает новый объект UserPublic, копируя только те поля, которые есть в UserPublic. Пароль не копируется."""
    return [UserPublic(**user.model_dump()) for user in data.get_all()]


def get_one(username: str) -> UserPublic:
    user = data.get_one(username)
    if not user:
        raise Missing(f"User {username} not found")
    return UserPublic(**user.model_dump())

def create(user: UserCreate) -> UserPublic:
    existing = data.get_one(user.username)
    if existing:
        raise Duplicate(f"User {user.username} exists")
    password_hash = get_password_hash(user.password)
    
    user_in_db = UserInDB(
        **user.model_dump(),
        id=0,
        password_hash=password_hash,
        avatar_url=None,
        bio=None,
        created_at=datetime.now(timezone.utc),
        updated_at=None,
        last_login=None,
        is_active=True,
        is_verified=False        
    )
    created = data.create(user_in_db)
    return UserPublic(**created.model_dump())

def replace(username: str, user: UserCreate) -> UserPublic:
    old_user = data.get_one(username)
    if not old_user:
        raise Missing(f"User {username} not found")
    if username != user.username:
        existing = data.get_one(user.username)
        if existing:
            raise Duplicate(f"User {user.username} exists")
    
    password_hash = get_password_hash(user.password)
    
    user_in_db = UserInDB(
        **user.model_dump(),
        id=old_user.id,
        password_hash=password_hash,
        avatar_url=old_user.avatar_url,
        bio=old_user.bio,
        created_at=old_user.created_at,
        updated_at=datetime.now(timezone.utc),
        last_login=old_user.last_login,
        is_active=old_user.is_active,
        is_verified=old_user.is_verified
    )
    
    updated = data.replace(username, user_in_db)
    return UserPublic(**updated.model_dump())

def delete(username: str):  
    user = data.get_one(username)
    if not user:
        raise Missing(f"User {username} not found")
    data.delete(username)