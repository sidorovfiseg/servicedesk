# Сервис для работы с пользователями

docker compose --env-file env/db.env -f docker-compose.yml -p service-desk up --build servicedesk-user-service-postgres servicedesk-user-service

alembic revision --autogenerate -m "First migration"
alembic revision -m ""
alembic upgrade head
