# Backend для игры "Социальная дилемма" (Prisoner's Dilemma)

Этот проект представляет собой бэкенд для игры "Социальная дилемма" с использованием FastAPI.

## Установка и запуск
### Локальная установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo/backend
   ```

2. Соберите и запустите контейнеры с помощью Docker Compose:
Соберите Docker-образ:
```bash
docker build -t social-dilemma-backend .
```

3. Запустите контейнер:
```bash
docker run -p 8000:8000 social-dilemma-backend
```
### API
#### Получение частот стратегий
- URL: /frequencies
- Метод: GET
- Описание: Возвращает историю частот стратегий.

#### WebSocket
- URL: /ws
- Метод: WebSocket
- Описание: WebSocket endpoint для реального времени обмена сообщениями.