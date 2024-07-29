# -*- coding: utf-8 -*-
from fastapi import FastAPI, Path    # Установили фреймворк FastAPI при помощи пакетного менеджера pip.
from typing import Annotated


app = FastAPI()    # Создали приложение(объект) FastAPI предварительно импортировав класс для него.


@app.get("/")  # если мы получили .get("/")-гет запрос
async def welcome() -> dict:  # то отработай эту функцию
    return {"message": "Hello world!"}


@app.get("/")    # Создайли маршрут к главной странице - "/".
async def Get_Main_Page() -> dict:
    return {"message": "Главная страница"}   # По нему должно выводиться сообщение "Главная страница".


@app.get("/user/admin}")    # Создайте маршрут к странице администратора - "/user/admin".
async def Get_Admin_Page() -> dict:
    return {"message": f"Вы вошли как администратор!"}  # По нему должно вывод-ся сообщение "Вы вошли как администратор"


@app.get("/user/user_id")  # Создали маршрут к страницам поль-й ис-я параметр в пути - "/user/{user_id}
async def Get_User_Number(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}
    # По нему должно выводиться сообщение "Вы вошли как пользователь № <user_id>".


@app.get("/user")   # Создайте маршрут к страницам пользователей передавая данные в адресной строке - "/user".
async def Get_User_Info(username: str, age: int) -> dict:
    return {"message": f"Информация о пользователе {username}", "Age": age}
    # По нему должно выводиться сообщение "Информация о пользователе. Имя: <username>, Возраст: <age>".


@app.get("/user/{user-id}")  # если мы получили .get("/")-гет запрос
async def Get_Main_Page(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", example="1")]) -> dict:
    # Path - провер.какой тип данных приходит и хранит их, Annotated - помогает работать с большестроками
    return {"message": f"Hello, {user_id}"}


@app.get("/user/{username}/{age}")  # если мы получили .get("/")-гет запрос
async def Get_Main_Page(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",
                        example="UrbanUser")], age: int = Path(ge=18, le=120,
                        description="Enter age", example="24")) -> dict:
    # Path - проверяет какой тип данных приходит и хранит их, Annotated - помогает работать с большестроками
    return {"message": f"Hello, {username} {age}"}

####################################################
# @app.get("/id")
# async def id_paginator(username: str = 'Alex', age: int = 34) -> dict:  # передаём по умолчанию
#     return {"User": username, "Age": age}
