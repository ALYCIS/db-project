import uuid
from typing import Any

from tenacity import retry_if_exception_type, wait_fixed, stop_after_attempt, retry

from ac_db.exceptions import DbOperationalError
from ac_db.models.migration import Migration
from ac_db.services.abstract_service import Service


class MigrationService(Service):

    def __init__(self, session):
        """

        :param session:
        """
        Service.__init__(self, session=session, table=Migration)

    @retry(reraise=True, retry=retry_if_exception_type(DbOperationalError), wait=wait_fixed(2), stop=stop_after_attempt(2))
    def get(self, ressource_id):
        """
        Gene
        :param ressource_id:
        :return:
        """
        return self.list(migration_id=ressource_id).one()

    @retry(reraise=True, retry=retry_if_exception_type(DbOperationalError), wait=wait_fixed(2), stop=stop_after_attempt(2))
    def get_migration(self, **kwargs):
        """
        get an migration
        :param kwargs:
        :return:
        """
        return self.list(**kwargs).one()

    @retry(reraise=True, retry=retry_if_exception_type(DbOperationalError), wait=wait_fixed(2), stop=stop_after_attempt(2))
    def delete_migration(self, migration):
        """
        deletes migration
        :param migration:
        :return:
        """
        try:
            uuid.UUID(migration)
            filters = {'migration_uuid': migration}
        except (AttributeError, ValueError):
            filters = {'migration_id': migration}
        Service.delete(**filters)

    def format_filters(self, additional_filters=None, step_numbers=None, step_state=None, **kwargs) -> Any:
        """

        :param additional_filters:
        :param step_numbers:
        :param step_state:
        :param kwargs:
        :return:
        """
        filters = Service.format_filters(self=self, additional_filters=additional_filters, **kwargs)

        if step_numbers:
            step_numbers_filter = self._filter(column_name="step_number", value=step_numbers, table=Step)