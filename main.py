from fastapi import FastAPI    # Установили фреймворк FastAPI при помощи пакетного менеджера pip.


app = FastAPI()    # Создали приложение(объект) FastAPI предварительно импортировав класс для него.


@app.get("/")    # Создали маршрут к главной странице - "/".
async def Get_Main_Page() -> dict:
    return {"message": "Главная страница"}   # По нему должно выводиться сообщение "Главная страница".


@app.get("/user/admin}")    # Создали маршрут к странице администратора - "/user/admin".
async def Get_Admin_Page() -> dict:
    return {"message": f"Вы вошли как администратор!"}  # По нему должно вывод-ся сообщение "Вы вошли как администратор"


@app.get("/user/user_id")  # Создали маршрут к страницам поль-й ис-я параметр в пути - "/user/{user_id}
async def Get_User_Number(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}
    # По нему должно выводиться сообщение "Вы вошли как пользователь № <user_id>".


@app.get("/user")   # Создали маршрут к страницам пользователей передавая данные в адресной строке - "/user".
async def Get_User_Info(username: str, age: int) -> dict:
    return {"message": f"Информация о пользователе {username}", "Age": age}
    # По нему должно выводиться сообщение "Информация о пользователе. Имя: <username>, Возраст: <age>".



# @app.get("/id")
# async def id_paginator(username: str = 'Alex', age: int = 34) -> dict:  # передаём по умолчанию
#     return {"User": username, "Age": age}
