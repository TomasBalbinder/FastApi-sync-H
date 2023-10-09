from sqlalchemy.orm import Session
from . import models, schemas
from uuid import UUID
from app.schemas import CosmonautUpdate


def get_cosmonauts(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.Cosmonaut).offset(skip).limit(limit).all()

def create_cosmonaut(db: Session, cosmonaut: schemas.Cosmonaut):
    db_cosmonaut = models.Cosmonaut(
        name=cosmonaut.name,
        age=cosmonaut.age,
        gender=cosmonaut.gender)
    db.add(db_cosmonaut)
    db.commit()
    db.flush()
    return db_cosmonaut

def delete_cosmonaut(db: Session, cosmonaut_id: UUID):
    cosmonaut = db.query(models.Cosmonaut).filter(models.Cosmonaut.id == cosmonaut_id).first()
    if cosmonaut:
        db.delete(cosmonaut)
        db.commit()
        db.flush()
    return cosmonaut

def update_cosmonaut(db: Session, cosmonaut_id: UUID, cosmonaut_update: CosmonautUpdate):
    cosmonaut = db.query(models.Cosmonaut).filter(models.Cosmonaut.id == cosmonaut_id).first()
    if cosmonaut:
        for key, value in cosmonaut_update.dict().items():
            setattr(cosmonaut, key, value)
        db.commit()
        db.flush()
    return cosmonaut


