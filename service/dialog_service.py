from config.db_config import connection


def create_table_if_not_exists():
    with connection as conn:
        command = ("CREATE TABLE IF NOT EXISTS dialogs("
                   "sender_id INTEGER, "
                   "receiver_id INTEGER, "
                   "message TEXT, "
                   "FOREIGN KEY (sender_id) REFERENCES users(chat_id), "
                   "FOREIGN KEY (receiver_id) REFERENCES users(chat_id)"
                   ")")

        conn.execute(command)
