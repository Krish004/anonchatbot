from peewee import IntegerField, TextField, BigIntegerField, BooleanField

from model.base_model import BaseModel


class UserModel(BaseModel):
    user_id = BigIntegerField(primary_key=True)
    chat_id = BigIntegerField()
    sex = TextField()
    age = IntegerField()
    name = TextField(null=True)
    username = TextField(null=True)
    connected_with = BigIntegerField()
    message_count = IntegerField()
    number = TextField(null=True)
    is_enabled = BooleanField(default=False)
    likes = IntegerField()
    dislikes = IntegerField()
    reports = IntegerField()
    is_enabled_media = BooleanField(default=True)
    is_admin = BooleanField(default=False)
    invited = IntegerField()

    class Meta:
        table_name = "users"

    def __str__(self):
        return (f"user_id:{self.user_id}, chat_id: {self.chat_id}, sex: {self.sex}, age: {self.age},"
                f" name: {self.name}, username: {self.username}, connected_with: {self.connected_with}, "
                f"message_count: {self.message_count}, number - {self.number},"
                f"likes - {self.likes}, dislikes - {self.dislikes}, reports - {self.reports}, invited - {self.invited}"
                f"is_enabled_media - {self.is_enabled_media}, is_enabled - {self.is_enabled}, is_admin - {self.is_admin}")

    @classmethod
    def from_dict(cls, user_dict):
        if user_dict is None:
            return None

        return cls(**user_dict)

    def get_profile(self) -> str:
        return (f"#️⃣Thy id - {self.user_id}\n"
                f"👀Ім'я - {self.name}\n"
                f"👥Become - {'👨 Boy' if self.sex == 'MALE' else '👩 Girl'}\n"
                f"🔞Age - {self.age}\n\n"
                f"Scores of your dialogues:\n"
                f"👍 - {self.likes} 👎 - {self.dislikes} 🚨 - {self.reports}")
