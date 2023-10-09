from sqlalchemy.orm import Session
from . import models


def get_all_cosmonauts(db:Session):
    return db.query(models.Cosmonaut).all()