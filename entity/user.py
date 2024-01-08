class User:
    def __init__(self,
                 chat_id: int,
                 sex: str,
                 age: int,
                 username: str,
                 connected_with: int,
                 message_count: int):
        self.chat_id = chat_id
        self.sex = sex
        self.age = age
        self.username = username
        self.connected_with = connected_with
        self.message_count = message_count

    def __str__(self):
        return (f"chat_id: {self.chat_id}, sex: {self.sex}, age: {self.age}, username: {self.username}, "
                f"connected_with: {self.connected_with}, message_count: {self.message_count}")

    @classmethod
    def from_dict(cls, user_dict):
        if user_dict is None:
            return None

        return cls(**user_dict)
