# api_yatube
api_yatube
# API YaTube

## Описание проекта

API YaTube - это RESTful API для социальной сети YaTube, которая позволяет пользователям публиковать посты, комментировать их, подписываться на других авторов и объединять посты в тематические группы.

## Функциональность

- Публикация, просмотр, редактирование и удаление постов
- Комментирование постов и управление комментариями
- Группировка постов по темам
- Подписка на авторов
- Аутентификация по JWT-токену

## Технологии

- Python 3.7+
- Django
- Django REST Framework
- JWT аутентификация (Djoser)

## Установка и запуск

1. Клонировать репозиторий:
```
git clone https://github.com/username/api_yatube.git
```

2. Создать и активировать виртуальное окружение:
```
python -m venv venv
source venv/bin/activate  # для Linux/macOS
venv\Scripts\activate  # для Windows
```

3. Установить зависимости:
```
pip install -r requirements.txt
```

4. Выполнить миграции:
```
python manage.py migrate
```

5. Запустить сервер:
```
python manage.py runserver
```

## Документация API

После запуска документация API доступна по адресу:
```
http://127.0.0.1:8000/redoc/
```

## API endpoints

### Авторизация

- `POST /api/v1/jwt/create/` - получить JWT-токен
- `POST /api/v1/jwt/refresh/` - обновить JWT-токен
- `POST /api/v1/jwt/verify/` - проверить JWT-токен

### Посты

- `GET /api/v1/posts/` - получить список всех постов
- `POST /api/v1/posts/` - создать новый пост
- `GET /api/v1/posts/{id}/` - получить пост по id
- `PUT /api/v1/posts/{id}/` - обновить пост по id
- `PATCH /api/v1/posts/{id}/` - частично обновить пост по id
- `DELETE /api/v1/posts/{id}/` - удалить пост по id

### Комментарии

- `GET /api/v1/posts/{post_id}/comments/` - получить комментарии к посту
- `POST /api/v1/posts/{post_id}/comments/` - создать комментарий к посту
- `GET /api/v1/posts/{post_id}/comments/{id}/` - получить комментарий по id
- `PUT /api/v1/posts/{post_id}/comments/{id}/` - обновить комментарий
- `PATCH /api/v1/posts/{post_id}/comments/{id}/` - частично обновить комментарий
- `DELETE /api/v1/posts/{post_id}/comments/{id}/` - удалить комментарий

### Группы

- `GET /api/v1/groups/` - получить список всех групп
- `GET /api/v1/groups/{id}/` - получить информацию о группе по id

### Подписки

- `GET /api/v1/follow/` - получить список своих подписок
- `POST /api/v1/follow/` - подписаться на пользователя

## Примеры запросов

### Получение JWT-токена

```
POST /api/v1/jwt/create/
{
    "username": "username",
    "password": "password"
}
```

### Создание поста

```
POST /api/v1/posts/
{
    "text": "Текст поста",
    "group": 1
}
```

### Создание комментария

```
POST /api/v1/posts/1/comments/
{
    "text": "Текст комментария"
}
```

### Подписка на автора

```
POST /api/v1/follow/
{
    "following": "username"
}
```

## Автор

