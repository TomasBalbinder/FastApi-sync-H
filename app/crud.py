from sqlalchemy.orm import Session
from . import models, schemas


def get_cosmonauts(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.Cosmonaut).offset(skip).limit(limit).all()


def create_cosmonaut(db: Session, cosmonaut: schemas.Cosmonaut):
    db_cosmonaut = models.Cosmonaut(
        name=cosmonaut.name,
        age=cosmonaut.age,
        gender=cosmonaut.gender)
    db.add(db_cosmonaut)
    db.commit()
    db.refresh(db_cosmonaut)
    return db_cosmonaut

