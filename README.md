<div align="center">

# 🐈 QRKot · этап 2

**Асинхронный REST API благотворительного фонда на FastAPI — второй этап: добавлены пользователи, регистрация и JWT-аутентификация (FastAPI Users), разграничение прав**

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-async-009688?logo=fastapi&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0_async-D71F00?logo=sqlalchemy&logoColor=white)
![Tests](https://img.shields.io/badge/pytest-78%2F78_passed-2ea44f?logo=pytest&logoColor=white)

</div>

> Это промежуточная версия проекта. Итоговая версия с отчётами на Яндекс Диске — **[QRkot-spreadsheets](https://github.com/JuliaDJ1/QRkot-spreadsheets)**.
> Путь проекта: [cat-charity-1](https://github.com/JuliaDJ1/cat-charity-1) → [cat-charity-2](https://github.com/JuliaDJ1/cat-charity-2) → [QRkot-spreadsheets](https://github.com/JuliaDJ1/QRkot-spreadsheets).

## О проекте

Фонд собирает пожертвования на целевые проекты. Сервис автоматически распределяет каждое пожертвование по открытым проектам в порядке их создания (FIFO): остаток переходит в следующий проект, а проект закрывается, когда нужная сумма собрана.

## Возможности

- **Целевые проекты** — создание, изменение, удаление; запрет изменять закрытый проект и удалять проект с внесёнными средствами.
- **Пожертвования** — автоматическое инвестирование в открытые проекты.
- **Пользователи и роли** — регистрация, JWT-аутентификация (FastAPI Users); проекты создаёт и меняет только суперпользователь, пожертвования делают авторизованные пользователи.
- Валидация через Pydantic v2, миграции Alembic, документация Swagger / ReDoc.
- **78 из 78 автотестов** pytest проходят.

## Стек

Python 3.12 · FastAPI · SQLAlchemy 2.0 (async) · Alembic · Pydantic v2 · SQLite / aiosqlite · FastAPI Users · JWT · pytest

## Запуск

**Требования:** Python 3.10+ (проверено на 3.12).

```bash
git clone https://github.com/JuliaDJ1/cat-charity-2.git
cd cat-charity-2
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

alembic upgrade head
uvicorn app.main:app --reload
```

Документация API: http://127.0.0.1:8000/docs

### Тесты

```bash
pytest
```

## Основные эндпоинты

| Метод | URL | Описание |
|---|---|---|
| GET, POST | `/charity_project/` | список проектов / создать проект |
| PATCH, DELETE | `/charity_project/{id}` | изменить / удалить проект |
| GET, POST | `/donation/` | список пожертвований / пожертвовать |
| POST | `/auth/register`, `/auth/jwt/login` | регистрация и получение JWT |
| GET | `/donation/my` | мои пожертвования |

## Автор

**Вадим Гусейнов** — Python-разработчик (Backend) · [Telegram](https://t.me/eviliing)
