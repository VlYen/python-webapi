# repository interface / protocol
from typing import Protocol, TypeVar

T = TypeVar("T")

class ProtocolRepository(Protocol[T]):
    '''
    Protocol for a generic repository handling CRUD operations for entities of type T.
    '''
    def list(self) -> list[T]:
        """
        List all records.
        :return: A list of T instances."""
        pass

    def get_by_id(self, id: int) -> T | None:
        """
        Fetch a record by its ID.

        :param id: The ID of the record to fetch.
        :return: The record if found, otherwise None.
        """
        pass

    def create(self, entity: T) -> int:
        """
        Create a new record.

        :param entity: The record to create.
        :return: The ID of the created record."""
        pass

    def update(self, entity: T) -> int:
        """
        Update an existing record.

        :param entity: The record data to update.
        :return: The number of rows updated.
        """
        pass

    def delete(self, id: int) -> int:
        """
        Delete a record by its ID.

        :param id: The ID of the record to delete.
        :return: The number of rows deleted.
        """
        pass