import asyncio
import threading

from config import db_config
from model.queue_user_model import QueueUserModel
from model.user_model import UserModel
from repo import user_repo, dialog_repo, queue_repo
from service.bot_service import init_bot
from service.queue_service import start_queue_worker


def prepare_db():
    with db_config.db as db:
        db.create_tables([UserModel, QueueUserModel])


def delete_old_queue():
    queue_repo.delete_all()


if __name__ == '__main__':
    prepare_db()
    delete_old_queue()

    threading.Thread(target=start_queue_worker, daemon=True).start()
    asyncio.run(init_bot())
