# repository interface / protocol
from typing import Protocol

from models.school_class_model import SchoolClassModel

class SchoolClassRepository(Protocol):
    def list_classes(self) -> list[SchoolClassModel]:
        """
        List all classes.
        :return: A list of SchoolClassModel instances."""
        pass

    def get_class_by_id(self, class_id: int) -> SchoolClassModel | None:
        """
        Fetch a class by its ID.

        :param class_id: The ID of the class to fetch.
        :return: The class if found, otherwise None.
        """
        pass

    def create(self, school_class: SchoolClassModel) -> int:
        """
        Create a new class.

        :param school_class: The class to create.
        :return: The ID of the created class."""
        pass

    def update(self, school_class: SchoolClassModel) -> int:
        """
        Update an existing class.

        :param school_class: The class data to update.
        :return: The number of rows updated.
        """
        pass

    def delete(self, class_id: int) -> int:
        """
        Delete a class by its ID.

        :param class_id: The ID of the class to delete.
        :return: The number of rows deleted.
        """
        pass