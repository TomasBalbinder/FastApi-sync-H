from sqlalchemy.orm import Session
from . import models


def get_cosmonauts(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.Cosmonaut).offset(skip).limit(limit).all()