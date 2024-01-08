class User:
    def __init__(self,
                 chat_id: int,
                 sex: str,
                 age: int,
                 name: str,
                 username: str,
                 connected_with: int,
                 message_count: int):
        self.chat_id = chat_id
        self.sex = sex
        self.age = age
        self.name = name
        self.username = username
        self.connected_with = connected_with
        self.message_count = message_count

    def __str__(self):
        return (f"chat_id: {self.chat_id}, sex: {self.sex}, age: {self.age}, name: {self.name}, "
                f"username: {self.username}, connected_with: {self.connected_with}, "
                f"message_count: {self.message_count}")

    @classmethod
    def from_dict(cls, user_dict):
        if user_dict is None:
            return None

        return cls(**user_dict)

    def get_profile(self) -> str:
        return f"""
#️⃣Твій id - {self.chat_id}
👀Ім'я - {self.name}
👥Стать - {'👨Хлопець' if self.sex == 'MALE' else '👩Дівчинка'}
🔞Вік - {self.age}
        """
