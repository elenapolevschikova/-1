from fastapi import FastAPI, status, Body, Path, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []  # Создаём пустой список, данные все запишим в users


# Создайте класс(модель) User, наследованный от BaseModel, который будет содержать следующие поля:
class User(BaseModel):  # содержит в себе
    id: int = None   # номер пользователя
    username: str       # имя пользователя
    age: int            # возраст пользователя


@app.get("/")  # если мы получили .get("/")-гет запрос, "Hello world!"
async def welcome() -> dict:  # то отработай эту функцию
    return {"user": "Hello world!"}


@app.get("/users")  # если мы получили .get("/")-гет запрос, теперь возвращает список users
def get_all_users() -> List[User]:  # возвращает список сообщений
    return users


@app.get("/user/{user_id}")  # если мы получили .get("/")-гет запрос
def get_user(user_id: int) -> User:  # то отработай эту функцию
    try:
        return users[user_id]  # возвращает конкретное сообщение которое у нас есть
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")  # или ловим ошибку


@app.post("/user/{username}/{age}")  # post запрос по маршруту '/user/{username}/{age}', теперь:
def create_user(username: str, age: int) -> User:   # Добавляет в список users объект User.

    # id этого объекта будет на 1 больше, чем у последнего в списке users. Если список users пустой, то 1.
    user_id = max(users, key=lambda x: int(x.id)).id + 1 if users else 1

    new_user = User(id=user_id, username=username, age=age)  # Создаем нового пользователя

    users.append(new_user)  # Добавляем пользователя в список

    return new_user  # Возвращаем созданного пользователя



@app.put('/user/{user_id}/{username}/{age}')  # put запрос по маршруту '/user/{user_id}/{username}/{age}' теперь:
def update_user(user_id: int, username: str, age: int) -> User:  # то отработай эту функцию
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user  # если пользователь с таким user_id есть в списке users и возвращает его.
    raise HTTPException(status_code=404, detail='User was not found.')


@app.delete("/user/{user_id}")  # если мы получили .get("/")-гет запрос, т.е.удаление сообщения
def delete_user(user_id: int) -> str:  # то отработай эту функцию
    try:
        users.pop(user_id)
        return f"User ID={user_id} deleted!"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")  # или ловим ошибку


@app.delete("/")  # если мы получили .get("/")-гет запрос, т.е.удаление сообщения
def kill_user_all() -> str:  # то отработай эту функцию
    users.clear()
    return "All User deleted!"
