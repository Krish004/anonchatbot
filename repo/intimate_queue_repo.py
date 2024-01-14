from model.intimate_queue_model import IntimateQueueModel


def create_table_if_not_exists() -> None:
    if not IntimateQueueModel.table_exists():
        IntimateQueueModel.create_table()


def add_user_to_queue(chat_id: int,
                      user_id: int,
                      sex: str,
                      sex_to_search: str) -> None:
    queue_user_model: IntimateQueueModel = IntimateQueueModel.create(
        chat_id=chat_id,
        user_id=user_id,
        sex=sex,
        sex_to_search=sex_to_search
    )

    queue_user_model.save()


def delete_all() -> None:
    IntimateQueueModel.delete().execute()


def get_all_users() -> [IntimateQueueModel]:
    return list(IntimateQueueModel.select().execute())


def remove_user_from_queue(chat_id: int) -> None:
    IntimateQueueModel.delete().where(IntimateQueueModel.chat_id == chat_id).execute()
