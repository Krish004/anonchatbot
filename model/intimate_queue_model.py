from peewee import BigIntegerField, TextField

from model.base_model import BaseModel


class IntimateQueueModel(BaseModel):
    user_id = BigIntegerField(primary_key=True)
    chat_id = BigIntegerField()
    sex = TextField()
    sex_to_search = TextField()

    class Meta:
        table_name = "intimate_queue"

    @classmethod
    def from_dict(cls, user_dict):
        if user_dict is None:
            return None

        return cls(**user_dict)

    def __str__(self):
        return (f"user_id - {self.user_id}, chat_id - {self.chat_id},"
                f" sex - {self.sex}, sex_to_search - {self.sex_to_search}")
