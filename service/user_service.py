from config.db_config import connection


def create_table_if_not_exists():
    with connection as conn:
        command = ('CREATE TABLE IF NOT EXISTS users('
                   'chat_id INTEGER PRIMARY KEY, '
                   'sex VARCHAR(25), '
                   'username TEXT, '
                   'connected_with INTEGER, '
                   'message_count INTEGER, '
                   'FOREIGN KEY (connected_with) REFERENCES users(chat_id)'
                   ')')

        conn.execute(command)
