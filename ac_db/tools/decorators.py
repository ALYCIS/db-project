from functools import wraps

from sqlalchemy.exc import OperationalError

from ac_db.exceptions import DbOperationalError


def check_operational(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except OperationalError as error:
            raise DbOperationalError(f'{error}') from error
    return wrapper
