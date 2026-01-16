from passlib.context import CryptContext 
from datetime import datetime, timezone, timedelta
from jose import JWTError, jwt
from typing import Optional
from src.model.user import UserInDB
import src.data.user as data

SECRET_KEY="72cc00294bb753b84c112af2fd8f1479f1a9ba08bd933f6b83e5a27ad1b735a9"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Хэширование
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# JWT
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    now = datetime.now(timezone.utc)
    if expires_delta:
        expire = now + expires_delta
    else:
        expire = now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_token(token: str) -> Optional[dict]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None

def get_username_from_token(token: str) -> Optional[str]:
    payload = decode_token(token)
    if payload and (username := payload.get("sub")):
        return username
    return None

# --- Аутентификация ---
def authenticate_user(username: str, password: str) -> Optional[UserInDB]:
    user = data.get_one(username)
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user

def get_current_user(token: str) -> Optional[UserInDB]:
    username = get_username_from_token(token)
    if not username:
        return None
    user = data.get_one(username)
    return user