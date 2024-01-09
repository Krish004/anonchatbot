from peewee import IntegerField, TextField, BigIntegerField

from model.base_model import BaseModel


class UserModel(BaseModel):
    chat_id = BigIntegerField(primary_key=True)
    sex = TextField()
    age = IntegerField()
    name = TextField()
    username = TextField()
    connected_with = BigIntegerField()
    message_count = IntegerField()

    class Meta:
        table_name = "users"

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
👥Стать - {'👨 Хлопець' if self.sex == 'MALE' else '👩 Дівчинка'}
🔞Вік - {self.age}
        """
