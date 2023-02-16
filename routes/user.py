from fastapi import APIRouter, Response
from config.db import conn
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT
import json

key = Fernet.generate_key()
passw = Fernet(key)

user = APIRouter()

@user.get("/users")
def get_users():
    result =  conn.execute(users.select()).fetchall().__str__()
    return result

@user.post("/users")
def create_user(user: User):
    new_user = {"name":user.name, "lastname":user.lastaname}
    new_user["password"] = passw.encrypt(user.password.encode("utf-8"))
    result = conn.execute(users.insert().values(new_user))
    conn.commit()
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first().__str__()

@user.get("/users/{id}")
def get_user(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first().__str__() 

@user.delete("/users/{id}")
def delete_user(id: str):
    conn.execute(users.delete().where(users.c.id == id))
    conn.commit()
    return Response(status_code=HTTP_204_NO_CONTENT)

@user.put("/users/{id}")
def update_user(id: str, user: User):
    conn.execute(users.update().values(name = user.name, lastname = user.lastaname, 
                                password = passw.encrypt(user.password.encode("utf-8")))
                                .where(users.c.id == id))
    conn.commit()
    return conn.execute(users.select().where(users.c.id == id)).first().__str__()