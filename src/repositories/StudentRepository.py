# repository interface / protocol
from typing import Protocol

from models.student_model import StudentModel

class StudentRepository(Protocol):
    def list_students(self) -> list[StudentModel]:
        """
        List all students.
        :return: A list of StudentModel instances."""
        pass

    def get_student_by_id(self, student_id: int) -> StudentModel | None:
        """
        Fetch a student by its ID.

        :param student_id: The ID of the student to fetch.
        :return: The student if found, otherwise None.
        """
        pass

    def create(self, student: StudentModel) -> int:
        """
        Create a new student.

        :param student: The student to create.
        :return: The ID of the created student."""
        pass

    def update(self, student: StudentModel) -> int:
        """
        Update an existing student.

        :param student: The student data to update.
        :return: The number of rows updated.
        """
        pass

    def delete(self, student_id: int) -> int:
        """
        Delete a student by its ID.

        :param student_id: The ID of the student to delete.
        :return: The number of rows deleted.
        """
        pass