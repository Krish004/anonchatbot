from model.queue_user_model import QueueUserModel


def create_table_if_not_exists() -> None:
    if not QueueUserModel.table_exists():
        QueueUserModel.create_table()


def add_user_to_queue(chat_id: int,
                      sex: str,
                      sex_to_search: str) -> None:
    queue_user_model: QueueUserModel = QueueUserModel.create(
        chat_id=chat_id,
        sex=sex,
        sex_to_search=sex_to_search
    )

    queue_user_model.save()


def delete_all() -> None:
    QueueUserModel.delete().execute()


def get_all_users() -> [QueueUserModel]:
    return QueueUserModel.select()


def remove_user_from_queue(chat_id: int) -> None:
    QueueUserModel.delete().where(chat_id=chat_id)
