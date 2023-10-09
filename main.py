from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
import app.models as models
import app.schemas as schemas
import app.crud as crud
from typing import List
from uuid import UUID
from app.schemas import CosmonautUpdate

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/cosmonauts/", response_model=List[schemas.Cosmonaut])
def read_cosmonauts(skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    cosmonauts = crud.get_cosmonauts(db, skip=skip, limit=limit)
    return cosmonauts

@app.post("/cosmonauts/", response_model=schemas.Cosmonaut)
def create_cosmonaut(cosmonaut: schemas.Cosmonaut, db: Session = Depends(get_db)):
    created_cosmonaut = crud.create_cosmonaut(db, cosmonaut)
    return created_cosmonaut

@app.delete("/cosmonauts/{cosmonaut_id}", response_model=schemas.Cosmonaut)
def delete_cosmonaut(cosmonaut_id: UUID, db: Session = Depends(get_db)):
    cosmonaut = crud.delete_cosmonaut(db, cosmonaut_id)
    if cosmonaut is None:
        raise HTTPException(status_code=404, detail="Cosmonaut not found")
    crud.delete_cosmonaut(db, cosmonaut_id)
    return cosmonaut

@app.put("/cosmonauts/{cosmonaut_id}", response_model=schemas.Cosmonaut)
def update_cosmonaut(cosmonaut_id: UUID, cosmonaut_update: CosmonautUpdate, db: Session = Depends(get_db)):
    updated_cosmonaut = crud.update_cosmonaut(db, cosmonaut_id, cosmonaut_update)
    if not updated_cosmonaut:
        raise HTTPException(status_code=404, detail="Cosmonaut not found")
    return updated_cosmonaut



