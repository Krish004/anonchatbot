import asyncio

from service import user_service, dialog_service, queue_service
from service.bot_service import init_bot


def prepare_db():
    user_service.create_table_if_not_exists()
    dialog_service.create_table_if_not_exists()
    queue_service.create_table_if_not_exists()


if __name__ == '__main__':
    prepare_db()
    asyncio.run(init_bot())
