class QueueUser:
    def __init__(self,
                 chat_id: int,
                 sex: str,
                 sex_to_search: str):
        self.chat_id = chat_id
        self.sex = sex
        self.sex_to_search = sex_to_search

    @classmethod
    def from_dict(cls, user_dict):
        if user_dict is None:
            return None

        return cls(**user_dict)

    def __str__(self):
        return f"chat_id - {self.chat_id}, sex - {self.sex}, sex_to_search - {self.sex_to_search}"
