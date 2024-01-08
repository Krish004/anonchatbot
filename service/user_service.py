from config.db_config import connection, cursor
from entity.user import User


def create_table_if_not_exists() -> None:
    """ Creates user table if not exists """
    with connection:
        command = ('CREATE TABLE IF NOT EXISTS users('
                   'chat_id INTEGER PRIMARY KEY, '
                   'sex VARCHAR(25), '
                   'age INTEGER, '
                   'username TEXT, '
                   'connected_with INTEGER, '
                   'message_count INTEGER, '
                   'FOREIGN KEY (connected_with) REFERENCES users(chat_id)'
                   ')')

        cursor.execute(command)
        connection.commit()


def create_user(user) -> None:
    """ Saves user to DB """
    with connection:
        command = ("INSERT INTO users "
                   "(username, chat_id, sex) "
                   "VALUES (?, ?, ?)")
        cursor.execute(command, (user.username, user.chat_id, user.sex))
        connection.commit()


def user_exists(chat_id: int) -> bool:
    """ Returns true if user with the chat_id exists """
    with connection:
        command = 'SELECT * FROM users WHERE chat_id = ?'
        result = cursor.execute(command, (chat_id,)).fetchall()
        return bool(len(result))


def get_user_by_chat_id(chat_id: int) -> User | None:
    """ Returns user from DB """
    with connection:
        command = 'SELECT * FROM users WHERE chat_id = ?'
        result = cursor.execute(command, (chat_id,)).fetchone()
        return User.from_dict(dict(result))


def get_user_count() -> int:
    """ Return count of users in database """
    with connection:
        command = "SELECT COUNT(*) FROM users"
        result = cursor.execute(command).fetchone()
        return tuple(result)[0]


def update_user_sex(sex: str,
                    chat_id: int) -> None:
    """ Change user gender by chat_id """
    command = "UPDATE users SET sex=? WHERE chat_id=?"
    cursor.execute(command, (sex, chat_id,))
    connection.commit()


def increment_message_count(chat_id: int) -> None:
    """ Increment user's message count by chat id """
    command = "UPDATE users SET message_count = message_count + 1 WHERE chat_id = chat_id"
    cursor.execute(command, (chat_id,))
    connection.commit()


def get_top_users() -> list[User]:
    """ Return top 5 users by message count """
    command = "SELECT * FROM users ORDER BY message_count DESC LIMIT 5"
    result = cursor.execute(command).fetchall()

    users: [User] = []
    for user_dict in result:
        users.append(User.from_dict(dict(user_dict)))
    return users
