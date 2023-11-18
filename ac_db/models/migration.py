import datetime

from sqlalchemy import Column, INTEGER, String, DateTime, Boolean
from sqlalchemy.orm import relationship

from ac_db.models.base import Base


class Migration(Base):
    """
    Model for migration.
    """

    __tablename__ = "migration"

    migration_id = Column("migrationId", INTEGER, primary_key=True, nullable=False, autoincrement=True, )
    migration_uuid = Column("migrationUuid", String, primary_key=True, unique=True, nullable=False, )
    migration_requester = Column("migrationRequester", String, unique=False, nullable=False, )
    migration_requester_mail = Column("migrationRequesterMail", String, unique=False, nullable=True, )
    migration_backup_mail = Column("migrationBackupMail", String, unique=False, nullable=True, )
    migration_backup_user = Column("migrationBackupUser", String, unique=False, nullable=True, )
    migration_mailing_list = Column("migrationMailingList", String, unique=False, nullable=True, )
    migration_state = Column("migrationState", String, unique=False, nullable=False, )
    migration_step = Column("migrationStep", INTEGER, unique=False, nullable=False, default=0, )
    migration_source = Column("migrationSource", String, unique=False, nullable=False, )
    migration_target = Column("migrationTarget", String, unique=False, nullable=False, )
    migration_started_on = Column("migrationStartedOn", DateTime, default=datetime.datetime.utcnow())
    migration_ended_on = Column("migrationEndedOn", DateTime, nullable=True)
    migration_dry_run = Column("migrationDryRun", Boolean, default=True)
    migration_last_run = Column("migrationLastRun", DateTime, default=datetime.datetime.utcnow())
    migration_runs = Column("migrationRuns", INTEGER, default=1)
    migration_note = Column("migrationNote", DateTime, unique=False, default="", )
    #steps = relationship("Step", back_populates="migration")
    #flows = relationship("Flow", back_populates="migration")



