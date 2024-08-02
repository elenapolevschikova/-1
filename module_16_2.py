# -*- coding: utf-8 -*-
# № 16/4. Построение базового проекта. Часть 1. # Запуск в main

from fastapi import FastAPI, Path  # фреймворк
from typing import Annotated

app = FastAPI()  # апп равен названию нашему фреймворку

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/")  # если мы получили .get("/")-гет запрос
async def welcome() -> dict:  # то отработай эту функцию
    return {"message": "Hello world!"}


@app.get("/users")  # если мы получили .get("/")-гет запрос
async def get_users() -> dict:  # то отработай эту функцию
    return {"message": users}


# @app.get("/massage/{message_id}")  # если мы получили .get("/")-гет запрос
# async def get_message(message_id: str) -> dict:  # то отработай эту функцию
#     return users[message_id]


@app.post("/user/{username}/{age}")  # если мы получили .get("/")-гет запрос
async def post_user(username: str, age: int) -> str:  # то отработай эту функцию
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = username, age
    return f'User {username} is registered'


@app.put("/user/{user_id}/{username}/{age}")  # если мы получили .get("/")-гет запрос
async def update_user(user_id: str, username: str, age: int) -> str:  # то отработай эту функцию
    users[user_id] = username, age
    return f"The user {username} is update"


@app.delete("/user/{user_id}")  # если мы получили .get("/")-гет запрос
async def delete_user(user_id: str) -> str:  # то отработай эту функцию
    users.pop(user_id)
    return f"User with {user_id} was deleted"

# @app.delete("/")  # если мы получили .get("/")-гет запрос
# async def delete_all_messages() -> str:  # то отработай эту функцию
#     users.clear()
#     return "All messages deleted"

########################

# 1. GET '/users'
# {
# "1": "Имя: Example, возраст: 18"
# }
# 2. POST '/user/{username}/{age}' # username - UrbanUser, age - 24
# "User 2 is registered"
# 3. POST '/user/{username}/{age}' # username - NewUser, age - 22
# "User 3 is registered"
# 4. PUT '/user/{user_id}/{username}/{age}' # user_id - 1, username - UrbanProfi, age - 28
# "User 1 has been updated"
# 5. DELETE '/user/{user_id}' # user_id - 2
# "User 2 has been deleted"
# 6. GET '/users'
# {
# "1": "Имя: UrbanProfi, возраст: 28",
# "3": "Имя: NewUser, возраст: 22"
# }

############################
