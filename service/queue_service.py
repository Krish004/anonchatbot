from config.db_config import connection, cursor


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


def remove_user_from_queue(chat_id: int) -> None:
    with connection:
        command = "DELETE FROM queue WHERE chat_id=?"
        cursor.execute(command, (chat_id,))
        connection.commit()
