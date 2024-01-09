from datetime import datetime

from model.message_model import MessageModel


def create_table_if_not_exists():
    if not MessageModel.table_exists():
        MessageModel.create_table()


def save_message(chat_id_from: int,
                 chat_id_to: int,
                 message: str,
                 date: datetime) -> None:
    message_model: MessageModel = MessageModel.create(
        chat_id_from=chat_id_from,
        chat_id_to=chat_id_to,
        message=message,
        date=date
    )
    message_model.save()
