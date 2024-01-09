import asyncio

from config import db_config
from model.message_model import MessageModel
from model.queue_user_model import QueueUserModel
from model.user_model import UserModel
from repo import queue_repo, user_repo
from service.bot_service import init_bot
from service.queue_service import start_queue_worker


def prepare_db():
    with db_config.db as db:
        db.create_tables([UserModel, QueueUserModel, MessageModel])


def delete_old_queue():
    queue_repo.delete_all()
    user_repo.delete_connected_with_for_all()


async def main():
    await asyncio.gather(start_queue_worker(), init_bot())


if __name__ == '__main__':
    prepare_db()
    delete_old_queue()

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
