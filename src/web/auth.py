from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from src.service import auth as auth_service
from src.model.user import UserCreate
from src.service import user as user_service
from datetime import timedelta

router = APIRouter(prefix="/auth")

@router.post("/login", summary="User login to obtain JWT token", tags=["authentication"])
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth_service.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    token = auth_service.create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/register", status_code=201, summary="Register a new user", tags=["authentication"])
def register(user: UserCreate):
    created_user = user_service.create(user)
    return created_user
