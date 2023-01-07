# -*- encoding: utf-8 -*-
from typing import Optional
from fastapi import FastAPI, Depends, Path, HTTPException
import models
from fastapi.middleware.cors import CORSMiddleware
import handle_db
import datetime
from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get(path="/")
async def FastAPI():
    return {"message": "Hello World"}

# select user list


@app.get(path="/api/users")
async def get_list_user():
    print('@app.get(path="/api/users")')
    result = handle_db.select_all_user()
    return {
        "status": "OK",
        "data": result
    }

# create user


@app.post(path="/api/users")
async def post_user(user: User):
    result = handle_db.create_user(user.name, user.email, user.password)
    if result == 1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }

# select user


@app.get(path="/api/users/{user_id}")
async def get_user(user_id: str):
    print('@app.get(path="/api/users/{user_id}")')
    result = handle_db.select_user(user_id)
    if result == 1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }

# update user


@app.put(path="/api/users/{user_id}")
async def put_user(user_id: str, name: str, email: str, user_status: str):
    print('@app.get(path="/api/users/{user_id}")')
    result = handle_db.update_user(user_id, name, email, user_status)
    if result == 1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }

# delete user


@app.delete(path="/api/users/{user_id}")
async def delete_user(user_id: str):
    result = handle_db.delete_user(user_id)
    if result == 1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }
