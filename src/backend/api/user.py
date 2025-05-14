# User/auth endpoints

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from app.db import crud, schemas
from app.core.security import hash_password, verify_password, create_access_token, get_current_user
from sqlalchemy.orm import Session
from app.db.models import User
from app.db import models
from app.core.config import settings
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str
    first_name: str = ""
    last_name: str = ""
    date_of_birth: str = None

class AuthResponse(BaseModel):
    user: dict
    access_token: str
    token_type: str = "bearer"

@router.post("/register", response_model=AuthResponse)
def register_user(request: RegisterRequest, db: Session = Depends(crud.get_db)):
    # Check if user exists
    if crud.get_user_by_username(db, request.username):
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed = hash_password(request.password)
    user_dict = request.dict()
    user_dict["hashed_password"] = hashed
    del user_dict["password"]
    db_user = crud.create_user(db, user_dict)
    # Create customer entry
    customer_data = {
        "first_name": request.first_name,
        "last_name": request.last_name,
        "date_of_birth": request.date_of_birth,
        "email": request.email
    }
    crud.create_customer(db, customer_data)
    token = create_access_token({"sub": str(db_user.id), "username": db_user.username})
    return AuthResponse(user={"id": db_user.id, "username": db_user.username, "email": db_user.email}, access_token=token)

@router.post("/login", response_model=AuthResponse)
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(crud.get_db)):
    db_user = crud.get_user_by_username(db, form_data.username)
    if not db_user or not verify_password(form_data.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"sub": str(db_user.id), "username": db_user.username})
    return AuthResponse(user={"id": db_user.id, "username": db_user.username, "email": db_user.email}, access_token=token)

@router.post("/logout")
def logout_user():
    # For JWT, logout is handled on the client by deleting the token
    return {"message": "Logged out successfully"}
