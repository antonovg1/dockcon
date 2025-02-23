# Използване на Python 3.11 като базов образ
FROM python:3.11

# Задаване на работна директория
WORKDIR /app

# Копиране на всички файлове в контейнера
COPY . .

# Инсталиране на зависимостите
RUN pip install --no-cache-dir -r requirements.txt

# Излагане на порта, на който ще работи FastAPI
EXPOSE 8000

# Стартиране на FastAPI приложението с Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
