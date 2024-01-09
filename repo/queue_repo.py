from config.db_config import connection, cursor
from entity.queue_user import QueueUser


def create_table_if_not_exists() -> None:
    with connection:
        command = ('CREATE TABLE IF NOT EXISTS queue('
                   'chat_id INTEGER, '
                   'sex VARCHAR(25), '
                   'sex_to_search VARCHAR(25), '
                   'FOREIGN KEY (chat_id) REFERENCES users(chat_id)'
                   ')')

        cursor.execute(command)
        connection.commit()


def add_user_to_queue(chat_id: int,
                      sex: str,
                      sex_to_search: str) -> None:
    with connection:
        command = 'INSERT INTO queue (chat_id, sex, sex_to_search) VALUES (?, ?, ?)'
        cursor.execute(command, (chat_id, sex, sex_to_search,))
        connection.commit()


def get_all_users() -> [QueueUser]:
    with connection:
        command = "SELECT * FROM queue"
        result = cursor.execute(command)
        queue_user_list: [QueueUser] = []
        for queue_user_dict in result:
            queue_user_list.append(QueueUser.from_dict(dict(queue_user_dict)))

        return queue_user_list


def remove_user_from_queue(chat_id: int) -> None:
    with connection:
        command = "DELETE FROM queue WHERE chat_id=?"
        cursor.execute(command, (chat_id,))
        connection.commit()


def delete_all() -> None:
    with connection:
        command = "DELETE FROM queue WHERE chat_id > 0"
        cursor.execute(command)
        connection.commit()


def get_user_by_chat_id(chat_id: int) -> QueueUser | None:
    with connection:
        command = "SELECT * FROM queue WHERE chat_id=?"
        result = cursor.execute(command, (chat_id,))
        return QueueUser.from_dict(dict(result))
