from fastapi import APIRouter
from config.db import conn
from models.user import users
from schemas.user import User

user = APIRouter()

@user.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()

@user.get("/users")
def helloWorl():
    return "Hello World"

@user.get("/users")
def helloWorl():
    return "Hello World"

@user.get("/users")
def helloWorl():
    return "Hello World"

@user.get("/users")
def helloWorl():
    return "Hello World"