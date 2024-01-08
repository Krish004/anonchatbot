from config.db_config import connection


def create_table_if_not_exists():
    with connection as conn:
        command = ('CREATE TABLE IF NOT EXISTS queue('
                   'user_id INTEGER, '
                   'sex VARCHAR(25), '
                   'FOREIGN KEY (user_id) REFERENCES users(chat_id)'
                   ')')

        conn.execute(command)
