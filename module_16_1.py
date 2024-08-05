from fastapi import FastAPI, Path   # Установили фреймворк FastAPI при помощи пакетного менеджера pip.
from typing import Annotated

app = FastAPI()    # Создали приложение(объект) FastAPI предварительно импортировав класс для него.


@app.get("/")    # Создайли маршрут к главной странице - "/".
async def get_main_page() -> dict:
    return {"user": "Главная страница"}   # По нему должно выводиться сообщение "Главная страница".


@app.get("/user/admin")    # Создали маршрут к странице администратора - "/user/admin".
async def get_admin_page() -> dict:
    return {"user": f"Вы вошли как администратор !"}
    # По нему должно вывод-ся сообщение "Вы вошли как администратор"


@app.get("/user/{user_id}")  # Создали маршрут к страницам поль-й ис-я параметр в пути - "/user/{user_id}
async def get_user_number(user_id: int) -> dict:
    return {"user": f"Вы вошли как пользователь № {user_id}"}
    # По нему должно выводиться сообщение "Вы вошли как пользователь № <user_id>".


@app.get("/user/{username}/{age}")  # Созд. маршрут к стр. пользователей передавая данные в адресной строке - "/user"
async def get_user_info(username: str, age: int) -> dict:  # то отработай эту функцию
    return {"user": f"Hello, {username} {age}"}


