import time

from config.queue_config import *
from model.queue_user_model import QueueUserModel
from repo import queue_repo, user_repo


def start_queue_worker():
    """
    Current method infinity checks for new connections for chatting
    It iterates through queue and match dialogs
    """
    while True:
        queue_user_list: [QueueUserModel] = queue_repo.get_all_users()
        for i in range(0, len(queue_user_list) - 1):
            user_queue_i: QueueUserModel = queue_user_list[i]
            found = False
            for j in range(0, len(queue_user_list) - i - 1):
                user_queue_j: QueueUserModel = queue_user_list[j]
                if ((user_queue_i.chat_id != user_queue_j.chat_id)
                        and
                        ((user_queue_i.sex_to_search == 'RANDOM'
                          or user_queue_i.sex_to_search == user_queue_j.sex)
                         and
                         (user_queue_j.sex_to_search == 'RANDOM'
                          or user_queue_j.sex_to_search == user_queue_i.sex))):
                    """ If match """
                    user_repo.update_user_connected_with(chat_id=user_queue_i.chat_id,
                                                         connected_with=user_queue_j.chat_id)

                    user_repo.update_user_connected_with(chat_id=user_queue_j.chat_id,
                                                         connected_with=user_queue_i.chat_id)

                    queue_repo.remove_user_from_queue(chat_id=user_queue_i.chat_id)
                    queue_repo.remove_user_from_queue(chat_id=user_queue_j.chat_id)
                    found = True

                    break
            if found:
                break

        time.sleep(TIME_TO_SLEEP_FOR_QUEUE_SECONDS)
