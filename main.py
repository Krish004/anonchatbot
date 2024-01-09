import asyncio
import threading

from repo import user_repo, dialog_repo, queue_repo
from service.bot_service import init_bot
from service.queue_service import start_queue_worker


def prepare_db():
    user_repo.create_table_if_not_exists()
    dialog_repo.create_table_if_not_exists()
    queue_repo.create_table_if_not_exists()


def delete_old_queue():
    queue_repo.delete_all()


if __name__ == '__main__':
    prepare_db()
    delete_old_queue()

    threading.Thread(target=start_queue_worker, daemon=True).start()
    asyncio.run(init_bot())
