from peewee import BigIntegerField, TextField, DateTimeField

from model.base_model import BaseModel


class MessageModel(BaseModel):
    chat_id_from = BigIntegerField()
    chat_id_to = BigIntegerField()
    message = TextField(null=True)
    date = DateTimeField()

    class Meta:
        table_name = "messages"
