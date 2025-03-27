# API для социальной сети Yatube

## Описание

API-сервис для проекта Yatube, который позволяет пользователям создавать посты, комментарии, подписываться на авторов и работать с группами контента через программный интерфейс.

## Технологии
- Python 3.9
- Django 3.2
- Django REST Framework
- JWT-авторизация

## Возможности API
- Публикация постов
- Комментирование постов
- Подписка на авторов
- Фильтрация постов по группам
- Получение и обновление JWT-токенов

## Эндпоинты API
- `/api/v1/jwt/create/` — Получение JWT-токена
- `/api/v1/jwt/refresh/` — Обновление JWT-токена
- `/api/v1/jwt/verify/` — Проверка JWT-токена
- `/api/v1/posts/` — Работа с постами
- `/api/v1/posts/{post_id}/comments/` — Работа с комментариями поста
- `/api/v1/groups/` — Получение информации о группах
- `/api/v1/follow/` — Управление подписками

## Запуск проекта

### Клонирование репозитория
```
git clone https://github.com/your-username/api_yatube.git
cd api_yatube
```

### Создание и активация виртуального окружения
```
python -m venv venv
source venv/bin/activate  # для Linux/macOS
venv\Scripts\activate     # для Windows
```

### Установка зависимостей
```
pip install -r requirements.txt
```

### Применение миграций
```
cd yatube_api
python manage.py migrate
```

### Создание суперпользователя
```
python manage.py createsuperuser
```

### Запуск сервера
```
python manage.py runserver
```

## Документация API
После запуска сервера документация доступна по адресу http://127.0.0.1:8000/redoc/

## Примеры использования

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

### Получение списка постов
```
GET /api/v1/posts/
```

### Создание комментария к посту
```
POST /api/v1/posts/{post_id}/comments/
{
    "text": "Текст комментария"
}
```

### Подписка на автора
```
POST /api/v1/follow/
{
    "following": "username_автора"
}
```

## Авторизация

Для доступа к API необходимо получить JWT-токен через эндпоинт `/api/v1/jwt/create/`, передав валидные учетные данные. 
Полученный токен необходимо передавать в заголовке `Authorization: Bearer <token>` для всех запросов, требующих авторизации.

## Автор
Ваше Имя
