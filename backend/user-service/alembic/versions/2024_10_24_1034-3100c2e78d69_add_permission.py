"""add permission

Revision ID: 3100c2e78d69
Revises: baf3d6222b84
Create Date: 2024-10-24 10:34:38.744041

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3100c2e78d69"
down_revision: Union[str, None] = "baf3d6222b84"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

from app.db.models.permission import PermisssionType, AccessLevel


def upgrade() -> None:
    permissions = [
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Создавать заявки",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Настраивать уведомления для себя",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Объединять заявки",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Удалять заявки",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Просматривать только свои заявки",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Просматривать заявки своего подразделения",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Просматривать заявки своего подразделения с дочерним",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Просматривать заявки своей компании",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Просматривать все заявки",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Редактировать только свои заявки",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Редактировать заявки своего подразделения",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Редактировать заявки своего подразделения с дочерним",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Редактировать заявки своей компании",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Редактировать все заявки",
        },
        # Карточки заявки
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Переносить заявку в другие сервисы и менять ее тип",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Просматривать историю изменений",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Перевод в массовый инцедент",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Добавлять категорию на сервис",
        },
        # Карточки заявки. Исполнение заявок
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Может быть исполнителем заявок",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Назначать себя исполнителем",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Назначать исполнителей и группу исполнителей",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Назначать себя наблюдателем",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Назначать наблюдателей",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Назначать согласующих",
        },
        # Карточка заявки. Трудозатраты
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Просматривать стоимость работ",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Редактировать стоимость работ",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Редактировать чужие трудозатраты (часы и стоимость)",
        },
        # Системный полномочия
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Редактировать бизнес-процессы",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Редактировать пользователей, подразделения и группы исполнителей",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Просматривать пользователей, подразделения и группы исполнителей",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Создавать \ Редактировать пользователей своей компании",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Не ограничивать просмотр/редактирование пользователей/подразделений своим подразделением и нижестоящим",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Редактировать роли",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Редактировать настройки / обновлять систему",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Редактировать свой аккаунт",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Редактировать общие представления",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Редактировать базу знаний",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Редактировать классы обслуживания",
        },
        {
            "name": "cre",
            "permission_type": PermisssionType.ALL,
            "description": "Определять типы заявок",
        },
        # Только для исполнителей
        {
            "name": "watch_system_log",
            "permission_type": PermisssionType.EXECUTOR,
            "description": "Просматривать системный лог",
        },
        {
            "name": "show_main_section",
            "permission_type": PermisssionType.ALL,
            "description": "Показывать раздел <Главная>",
        },
        {
            "name": "show_knowledge_base_section",
            "permission_type": PermisssionType.ALL,
            "description": "Показывать раздел <База знаний>",
        },
        {
            "name": "show_assets_section",
            "permission_type": PermisssionType.ALL,
            "description": "Показывать раздел <Активы>",
        },
        {
            "name": "show_report_section",
            "permission_type": PermisssionType.ALL,
            "description": "Показывать все данные в разделе <Отчеты>",
        },
        {
            "name": "show_report_section",
            "permission_type": PermisssionType.ALL,
            "description": "Показывать данные по правам доступа на сервисы в разделе <Отчеты>",
        },
        {
            "name": "watch_assets",
            "permission_type": PermisssionType.ALL,
            "description": "Просматривать активы",
        },
        {
            "name": "edit_assets",
            "permission_type": PermisssionType.ALL,
            "description": "Редактировать только свои активы",
        },
        {
            "name": "edit_assets",
            "permission_type": PermisssionType.ALL,
            "description": "Редактировать активы своего подразделения",
        },
        {
            "name": "edit_assets",
            "permission_type": PermisssionType.ALL,
            "description": "Редактировать активы своей компании",
        },
        {
            "name": "edit_assets",
            "permission_type": PermisssionType.ALL,
            "description": "Редактировать все активы",
        },
        # Только для исполнителей
        {
            "name": "edit_services",
            "permission_type": PermisssionType.EXECUTOR,
            "description": "Редактировать все сервисы",
        },
        {
            "name": "edit_services",
            "permission_type": PermisssionType.EXECUTOR,
            "description": "Редактировать только сервисы, где пользователь является владельцем / заместителем",
        },
        # Интерфейс (права общие для клиентов и исполнителей)
        {
            # Стартовая страница - список заявок, иначе список сервисов
            "name": "main_page_is_request_list",
            "permission_type": PermisssionType.ALL,
            "description": "Стартовая страница - список  заявок",
        },
        {
            "name": "show_default_filters",
            "permission_type": PermisssionType.ALL,
            "description": "Показывать фильтры по умолчанию",
        },
    ]


def downgrade() -> None:
    pass
