from peewee import ModelSelect

from model.user_model import UserModel


def create_table_if_not_exists() -> None:
    if not UserModel.table_exists():
        UserModel.create_table()


def user_exists(chat_id: int) -> bool:
    query: ModelSelect = UserModel.select().where(UserModel.chat_id == chat_id)
    return len(query.execute()) > 0


def create_user(user_id: int,
                chat_id: int,
                username: str) -> None:
    user_model: UserModel = UserModel.create(
        user_id=user_id,
        chat_id=chat_id,
        sex='MALE',
        age=18,
        name='',
        username=username,
        message_count=0
    )
    user_model.save()


def get_user_by_chat_id(chat_id: int) -> UserModel | None:
    return UserModel.select().where(UserModel.chat_id == chat_id).get()


def update_user_sex(sex: str,
                    chat_id: int) -> None:
    UserModel.update(sex=sex).where(UserModel.chat_id == chat_id).execute()


def update_user_age(age: int,
                    chat_id: int) -> None:
    UserModel.update(age=age).where(UserModel.chat_id == chat_id).execute()


def update_user_name(name: str,
                     chat_id: int) -> None:
    UserModel.update(name=name).where(UserModel.chat_id == chat_id).execute()


def update_user_connected_with(chat_id: int,
                               connected_with: int) -> None:
    UserModel.update(connected_with=connected_with).where(UserModel.chat_id == chat_id).execute()


def update_user_number(number: str,
                       chat_id: int) -> None:
    UserModel.update(number=number).where(UserModel.chat_id == chat_id).execute()


def increment_user_message_count(chat_id: int) -> None:
    UserModel.update(message_count=UserModel.message_count + 1).where(UserModel.chat_id == chat_id).execute()


def delete_connected_with_for_all() -> None:
    UserModel.update(connected_with=0).execute()


def update_user_is_enabled(is_enabled: bool,
                           chat_id: int):
    UserModel.update(is_enabled=is_enabled).where(UserModel.chat_id == chat_id).execute()


def increment_user_likes(chat_id: int):
    UserModel.update(likes=UserModel.likes + 1).where(UserModel.chat_id == chat_id).execute()


def increment_user_dislikes(chat_id: int):
    UserModel.update(dislikes=UserModel.dislikes + 1).where(UserModel.chat_id == chat_id).execute()


def increment_user_reports(chat_id: int):
    UserModel.update(reports=UserModel.reports + 1).where(UserModel.chat_id == chat_id).execute()


def update_user_is_enabled_media(chat_id: int,
                                 is_enabled_media: bool):
    UserModel.update(is_enabled_media=is_enabled_media).where(UserModel.chat_id == chat_id).execute()


def increment_user_invited(chat_id: int):
    UserModel.update(invited=UserModel.invited + 1).where(UserModel.chat_id == chat_id).execute()
