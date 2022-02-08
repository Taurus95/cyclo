import sys
from cyclo.utils.logger import logger
from peewee import *
from cyclo.config.constants import (
    DATABASE
)
from cyclo.models import *
from datetime import datetime

db = SqliteDatabase(DATABASE)

def app():
    """Main function"""
    try:
        """Run user's input command."""
        # Initial log values
        logger.debug("### NEW PROCESS STARTED ###")
        # logger.debug(sys.argv)
        # Call the app
        Cyclo()

    except KeyboardInterrupt:
        print("\nQuitting...")
        sys.exit(1)

class Cyclo():
    def __init__(self):

        route = Route.create(start=datetime.now())
        print(f"Initializing new route. ID:{route.id}")
        try:
            while True:
                # Check coord
                # If coord is not different dont create a new, it is a stop
                # Detect plate number, if exist one different wait for the distance

                pass
        except KeyboardInterrupt:
            print("\nQuitting...")
            route.update(end=datetime.now())
            sys.exit(1)

    def configure_db(self):
        db.connect()
        db.create_tables([Coord, Event, Route])
        db.close()

    def check_sensors(self):
        return True
