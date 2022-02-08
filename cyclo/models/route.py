from peewee import *
import datetime
from cyclo.config.constants import (
    DATABASE
)

db = SqliteDatabase(DATABASE)

class Route(Model):
    start = DateTimeField(default=datetime.datetime.now)
    end = DateTimeField(null = True)
    average_speed = DecimalField(null = True)
    max_speed = DecimalField(null = True)
    initial_altitude = DecimalField(null = True)
    final_altitude = DecimalField(null = True)
    max_altitude = DecimalField(null = True)

    class Meta:
        database = db
