from typing import Union

from fastapi import FastAPI, Depends, HTTPException

from pydantic import BaseModel

from sqlalchemy import create_engine,text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from database import setup_db
from person import models, schemas, repo

_db_deps = setup_db()
app = FastAPI()


models.Base.metadata.create_all(bind=_db_deps["engine"])

def get_db():
    session = _db_deps["SessionLocal"]
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health_check():
    try:
        with _db_deps["engine"].connect() as connection:
            connection.execute(text("SELECT 1"))
        return {"status": "healthy"}            
    except SQLAlchemyError:
        return {"status": "unhealthy"}

# persons resource

@app.post("/persons/", response_model=schemas.Person)
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    return repo.create_person(db=db, person=person)

@app.get("/persons/{person_id}", response_model=schemas.Person)
def read_person(person_id: int, db: Session = Depends(get_db)):
    db_person = repo.get_person(db, person_id=person_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person

@app.put("/persons/{person_id}", response_model=schemas.Person)
def update_person(person_id: int, person: schemas.PersonUpdate, db: Session = Depends(get_db)):
    db_person = repo.update_person(db=db, person_id=person_id, person=person)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person

@app.delete("/persons/{person_id}", response_model=schemas.Person)
def delete_person(person_id: int, db: Session = Depends(get_db)):
    db_person = repo.delete_person(db=db, person_id=person_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person
