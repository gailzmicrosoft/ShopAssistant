# CRUD operations for database access
from . import models
from sqlalchemy.orm import Session

# User CRUD

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: dict):
    db_user = models.User(
        username=user["username"],
        email=user["email"],
        hashed_password=user["hashed_password"],
        first_name=user.get("first_name"),
        last_name=user.get("last_name"),
        date_of_birth=user.get("date_of_birth"),
        is_active=user.get("is_active", True)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Product CRUD

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

# ...additional CRUD for cart, orders, wishlist, chat, etc. to be implemented
