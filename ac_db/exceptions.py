"""Module manage exception for this project """


class DbError(Exception):
    """ Exception that inherit from base exception """

    def __init__(self, message):
        super().__init__(message)
        self.message: str = message


class DbOperationalError(DbError):
    pass
