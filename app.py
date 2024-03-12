from fastapi import FastAPI, HTTPException
from uuid import UUID, uuid4
from typing import List
from models import User, Role

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("a6426b1d-3e67-4900-8ee7-84cde2f8b191"),
        first_name="Ana", 
        last_name= "Maria", 
        email="email@gmail.com", 
        role=[Role.role_1]
        ),
    User(
        id=UUID("ff603557-a5b1-4cba-b4df-34a156eae3df"),
        first_name="Cintia", 
        last_name= "Moreira", 
        email="email2@gmail.com", 
        role=[Role.role_2]
        ),
     User(
        id=UUID("60999b80-7b69-4089-9aad-9a49f8aa47c5"),
        first_name="Camila", 
        last_name= "Silva", 
        email="email3@gmail.com", 
        role=[Role.role_3]
        ),
]

@app.get("/")
async def root():
    return{"mensagem":"Olá paula!"}

@app.get("/api/users")
async def get_users():
    return db;

@app.get("/api/users/{id}")
async def get_users(id: UUID):
    for user in db:
        if user.id ==id:
            return user
    return {"mensagem":"Usuario não encontrado!"}

@app.post("/api/users")
async def add_users(user: User):
     db.append(user)
     return{"id": user.id}

@app.delete("/api/users/{id}")
async def remove_user(id: UUID):
    for user in db: 
        if user.id == id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code=404,
        detail=f"Usuario com o {id} não encontardo!"
    )
