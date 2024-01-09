from peewee import ModelSelect

from model.user_model import UserModel


def create_table_if_not_exists() -> None:
    if not UserModel.table_exists():
        UserModel.create_table()


def user_exists(chat_id: int) -> bool:
    query: ModelSelect = UserModel.select().where(UserModel.chat_id == chat_id)
    return len(query.execute()) > 0


def create_user(chat_id: int,
                username: str) -> None:
    user_model: UserModel = UserModel.create(
        chat_id=chat_id,
        sex='MALE',
        age=18,
        name='',
        username=username,
        message_count=0
    )
    user_model.save()


def get_user_by_chat_id(chat_id: int) -> UserModel | None:
    return UserModel.get_by_id(chat_id)


def update_user_sex(sex: str,
                    chat_id: int) -> None:
    UserModel.update(sex=sex).where(UserModel.chat_id == chat_id).execute()


def update_user_age(age, chat_id) -> None:
    UserModel.update(age=age).where(UserModel.chat_id == chat_id).execute()


def update_user_name(name: str,
                     chat_id: int) -> None:
    UserModel.update(name=name).where(UserModel.chat_id == chat_id).execute()


def update_user_connected_with(chat_id, connected_with) -> None:
    UserModel.update(connected_with=connected_with).where(UserModel.chat_id == chat_id).execute()
