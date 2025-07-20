from sqlalchemy.orm import Session
from app import models, schemas
from passlib.hash import bcrypt


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
    db_user = models.User(
        email=user.email,
        password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
