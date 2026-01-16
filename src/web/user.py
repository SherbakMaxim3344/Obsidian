from fastapi import APIRouter, status, HTTPException
from src.model.user import UserCreate, UserPublic, UserInDB
from src.service import user as service
from errors import Missing as errorMissing
from errors import Duplicate as errorDuplicate

router = APIRouter(prefix= "/users")

@router.get("") #/user
@router.get("/", response_model=list[UserPublic], summary="Get all users", tags=["users"]) #/user/
def get_all() -> list[UserPublic]:
    return service.get_all()

@router.get("/{username}", response_model=UserPublic, summary="Get user by username", tags=["users"])
def get_one(username: str) -> UserPublic:
    try:
        return service.get_one(username)
    except errorMissing:
        raise HTTPException(status_code=404, detail=f"User {username} not found")

@router.post("/", response_model=UserPublic,status_code=201, summary="Create a new user", tags=["users"])
def create(user: UserCreate) -> UserPublic:
    try:
        return service.create(user)
    except errorDuplicate:
        raise HTTPException(status_code=409, detail=f"user {user.username} already exists")

@router.put("/{username}", response_model=UserPublic, summary="Update an existing user", tags=["users"])
def update_user(username: str, user: UserCreate) -> UserPublic:
    try:
        return service.replace(username, user)
    except errorMissing:
        raise HTTPException(status_code=404, detail=f"User {username} not found")

@router.delete("/{username}", status_code=204, summary="Delete a user", tags=["users"])
def delete(username: str):
    try:
        service.delete(username)
        return None
    except errorMissing:
        raise HTTPException(status_code=404, detail=f"User {username} not found")
        