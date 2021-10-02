from peewee import *
from cyclo.config.constants import (
    DATABASE
)

db = SqliteDatabase(DATABASE)

class Coord(Model):
    latitude = IntegerField()
    longitud = IntegerField()
    altitude = IntegerField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
