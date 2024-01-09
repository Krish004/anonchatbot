from peewee import Model

from config.db_config import db


class BaseModel(Model):
    class Meta:
        database = db
