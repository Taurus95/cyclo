from peewee import *
from cyclo.config.constants import (
    DATABASE
)
from .coord import Coord

db = SqliteDatabase(DATABASE)

class Event(Model):
    kind = CharField()
    coord = ForeignKeyField(Coord)

    class Meta:
        database = db
