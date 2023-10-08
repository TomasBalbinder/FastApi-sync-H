from fastapi import FastAPI, HTTPException
from models import Cosmonaut
from typing import List
from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
import database
from schemas import Gender

app = FastAPI()




def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()




"""@app.get('/cosmonauts')
async def view_cosmonauts():
    return db


@app.post('/cosmonauts')
async def add_cosmonaut(cosmonaut : Cosmonaut):
    db.append(cosmonaut)
    return {"id" : cosmonaut.id }


@app.delete('/cosmonauts/{cosmonaut_id}')
async def delete_cosmonaut(cosmonaut_id : UUID):
    for cosmonaut in db:
        if cosmonaut.id == cosmonaut_id:
            db.remove(cosmonaut)
            return {"Cosmonaut successfully deleted"}
        
    raise HTTPException(
        status_code=404, detail=f"User with id {cosmonaut_id} was deleted")


@app.put('/cosmonauts/{cosmonaut_id}')
async def update_cosmonaut(cosmonaut_update : CosmonautUpdate,cosmonaut_id : UUID):
    for cosmonaut in db:
        if cosmonaut.id == cosmonaut_id:
            if cosmonaut_update.name is not None:
                cosmonaut.name = cosmonaut_update.name
            if cosmonaut_update.age is not None:
                cosmonaut.age = cosmonaut_update.age
            if cosmonaut_update.gender is not None:
                cosmonaut.gender = cosmonaut_update.gender
            return
    raise HTTPException(
        status_code=404, detail=f"User with id {cosmonaut_id} doesn't exist")"""



