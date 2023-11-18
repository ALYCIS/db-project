import dataclasses
from typing import Optional

from ac_db.models.model import Model
from ac_db.tools.session import SqlAlchemySession


@dataclasses.dataclass
class Postgres(Model):
    db_address: Optional[str] = None
    db_name: Optional[str] = None
    db_port: Optional[int] = None
    db_password: Optional[str] = None
    db_user: Optional[str] = None
    client_encoding: str = 'utf8'
    max_overflow: int = 20
    pool_pre_ping: bool = True
    pool_size: int = 10
    __database = None

    @property
    def database(self):
        if self.__database is None:
            self.__database = SqlAlchemySession(db_address=self.db_address, db_name=self.db_name, db_password=self.db_password,
                                                pool_size=self.pool_size, pool_pre_ping=self.pool_pre_ping,
                                                client_encoding=self.client_encoding, db_port=self.db_port, db_user=self.db_user,
                                                max_overflow=self.max_overflow, database_type='postgresql')
