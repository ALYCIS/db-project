import dataclasses

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@dataclasses.dataclass
class SqlAlchemySession:
    db_address: str
    db_user: str
    db_password: str
    db_port: int
    db_name: str
    pool_size: int = 10
    pool_pre_ping: bool = True
    client_encoding: str = 'utf8'
    max_overflow: int = 20
    database_type: str = 'postgresql'

    def __post_init__(self):
        database = f'{self.database_type}://{self.db_user}:{self.db_password}@{self.db_address}:{self.db_port}/{self.db_name}'
        engine = create_engine(url=database, pool_pre_ping=self.pool_pre_ping, client_encoding=self.client_encoding,
                               pool_size=self.pool_size, max_overflow=self.max_overflow)
        self.session_maker = sessionmaker(bind=engine)

    def __del__(self):
        self.session_maker().close()
        del self
