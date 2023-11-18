""" Module to define constant schema """
from ac_db.tools.singleton import Singleton


class Constants(metaclass=Singleton):
    """Class representing a constant schema """
    def __init__(self):
        self.db_schema = None
