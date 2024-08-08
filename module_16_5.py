from fastapi import FastAPI, status, Body, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []  # данные все запишим в messages_db


class User(BaseModel):  # содержит в себе
    id: int = None         # айтишник
    text: str              # текст
    username: str
    age: int



@app.get("/")  # если мы получили .get("/")-гет запрос
def get_all_user(request: Request) -> HTMLResponse:  # возвращает список сообщений
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}")  # если мы получили .get("/")-гет запрос
def get_users(request: Request, user_id: int) -> HTMLResponse:  # возвращает список сообщений
    try:
        # возвращает конкретное сообщение которое у нас есть, но под конкретный message_id
        return templates.TemplateResponse("users.html", {"request": request, "user": users[user_id]})
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")  # или ловим ошибку


@app.post("/user/{username}/{age}", status_code=status.HTTP_201_CREATED)  # мы хотим создать сообщение
def create_user(request: Request, username: str, age: int, user: str = Form()) -> HTMLResponse:
    if users:
        user_id = max(users, key=lambda m: m.id).id + 1
    else:
        user_id = 0
    users.append(User(id=user_id, username=username, age=age, text=user))  # добавляем
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.put("/user/{user_id}/{username}/{age}")  # если мы получили .get("/")-гет запрос
def update_user(user_id: int, username: str, age: int, user: str = Body()) -> str:  # то отработай эту функцию
    try:
        edit_user = users[user_id]
        edit_user.username = username
        edit_user.age = age
        edit_user.text = user
        return f"User updated!"
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")  # или ловим ошибку


@app.delete("/user/{user_id}")  # если мы получили .get("/")-гет запрос, т.е.удаление сообщения
def delete_user(user_id: int) -> str:  # то отработай эту функцию
    try:
        users.pop(user_id)
        return f"User ID={user_id} deleted!"
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")  # или ловим ошибку


@app.delete("/")  # если мы получили .get("/")-гет запрос, т.е.удаление сообщения
def kill_user_all() -> str:  # то отработай эту функцию
    users.clear()
    return "All user deleted!"




