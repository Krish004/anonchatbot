from peewee import IntegerField, TextField

from model.base_model import BaseModel


class QueueUserModel(BaseModel):
    chat_id = IntegerField(primary_key=True)
    sex = TextField()
    sex_to_search = TextField()

    class Meta:
        table_name = "queue"

    @classmethod
    def from_dict(cls, user_dict):
        if user_dict is None:
            return None

        return cls(**user_dict)

    def __str__(self):
        return f"chat_id - {self.chat_id}, sex - {self.sex}, sex_to_search - {self.sex_to_search}"
