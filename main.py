'''CRUD'''
from typing import List
from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException
from models import Genero,User,Role


app = FastAPI();

db: List[User] = [
  User(
    id=uuid4(),
    nombre = 'Marco',
    apellido = 'Luna',
    genero = Genero.masculino,
    roles = [Role.admin]
  ),
  User(
    id=uuid4(),
    nombre = 'Zaseck',
    apellido = 'Cruz',
    genero = Genero.masculino,
    roles = [Role.user]
  ),
  User(
    id=uuid4(),
    nombre = 'Carlos',
    apellido = 'Aranda',
    genero = Genero.masculino,
    roles = [Role.user]
  ),
  User(
    id=uuid4(),
    nombre = 'Raul',
    apellido = 'Reyes',
    genero = Genero.masculino,
    roles = [Role.user]
  )
]


@app.get('/')
async def root():
  return {"message": "Welcome to the CRUD API"}

@app.get('/api/users')
async def get_users():
  return db

@app.post('/api/users')
async def create_user(user: User):
  db.append(user)
  return {'id':user.id}

@app.delete('/api/users/{id}')
async def delete_user(id: UUID):
  for user in db:
    if user.id == id:
      db.remove(user)
      return
    raise HTTPException(
      status_code=404, detail=f'Error al eliminar, id{id} no encontrado'
    )