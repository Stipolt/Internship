# Django Rest Framework Api
### DRF API для работы с базой данных Pereval(SF internship)

В данном проекте были реализованы основные функции DRFApi:
- GET запросы с получением всех или одного объекта
- POST запрос создающий объект в базе данных
- PATCH/PUT запросы редактирующие или заменяющие данные соответственно
- Добавлена авто документация swagger "***domain***"/swagger/


### Основные модели:
- Pereval - Главная модель проекта, добавляемая пользователем
- User - Непосредственно пользователь
- Image - Изображения перевалов
- Area - местность нахождения перевала
- Coord - Координаты

### Основные пути запросов

- ../submitData/create отправляет json с полным описанием объекта
- ../submitData/{id}/  GET запрос на объект модели Pereval(json)
- ../submitData/{id}/  PUT/PATCH - Замена/Редактирование
- ../submitData/{id}/  DELETE - Удаление


### Технологии

###### Стек используемых технологий:
 - Python
 - Django
 - Django Rest Framework


### Дополнительные библиотеки:
 - drf_yasg/swagger
 - phonenumbers
 - pillow



###### *Авто документация доступна по адресу:
 - "***domain***"/swagger/
 
Пример запроса:

```json
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
{
    "id": int,
    "image": [
        {
            "id": int,
            "image": "base64",
            "title": "string"
        }
    ],
    "area": [
        {
            "id": int,
            "title": "string"
        }
    ],
    "coord_id": {
        "id": int,
        "latitude": float,
        "longitude": float,
        "height": int
    },
    "user": {
        "id": id: int,
        "email": "email: str",
        "phone": "+phonenumber",
        "fam": "Surname: str",
        "name": "Name: str",
        "otc": "F.name str"
    },
    "add_time": "year-mm-dd",
    "beautyTitle": "string",
    "title": "string",
    "other_titles": "",
    "connect": "",
    "status": status: int,
    "level_winter": int,
    "level_spring": int, 
    "level_summer": int,
    "level_autumn": int
```
status: int, (1 -'new',2 - 'pending', 3 - 'accepted', 4 -'rejected')
level_: int, (1 - 1А, 2- 1Б, 3 - 2А, 4- 2Б, 5 - 3А, 6 -3Б)