# DockCon - FastAPI приложение с Docker и CI/CD

##  Описание
Това е FastAPI приложение, което използва PostgreSQL като база данни и има автоматизиран CI/CD pipeline с GitHub Actions.

##  Инсталация и стартиране

### 1 Клониране на репото:
\\\sh
git clone https://github.com/antonovg1/dockcon.git
cd dockcon
\\\

### 2 Стартиране с Docker:
\\\sh
docker-compose up --build -d
\\\

### 3 Проверка на работещите контейнери:
\\\sh
docker ps -a
\\\

##  Тестване с Pytest
\\\sh
docker exec -it fastapi_service pytest /app/tests
\\\

---
 **Проектът съдържа автоматизирани тестове и се изгражда чрез GitHub Actions.**
