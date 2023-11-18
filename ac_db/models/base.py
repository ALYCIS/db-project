import os

from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base

from ac_db.constants import Constants

metadata = MetaData(schema=os.getenv("DB_SCHEMA") or Constants().db_schema)
Base = declarative_base(metadata=metadata)
