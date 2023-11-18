"""This module manage database access. It is the only way where the database access is allowed """

import dataclasses
from typing import Optional

from ac_db.tools.postgres import Postgres


# pylint: disable=too-many-instance-attributes
@dataclasses.dataclass
class AcDb(Postgres):
    db_name: Optional[str] = None
    db_address = Optional[str] = None
    db_user: Optional[str] = None
    db_password: Optional[str] = None
    db_port: Optional[int] = None
    db_schema: Optional[str] = None
    pool_size: int = 10
    max_overflow: int = 20
    client_encoding: str = 'utf8'
    pool_pre_ping: bool = True

    def __post_init__(self):
        super().__init__(**{key: value for key, value in self.to_dict().items() if key != "db_schema"})
