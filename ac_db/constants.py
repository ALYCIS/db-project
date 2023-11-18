from ac_db.tools.singleton import Singleton


class Constants(metaclass=Singleton):

    def __init__(self):
        self.db_schema = None
