import logging
from factories.RepositoryFactory import RepositoryFactory
from models.student_model import StudentModel

logger = logging.getLogger(__name__)

class StudentService:
   def __init__(self, factory: RepositoryFactory):
      self.repo = factory.get_repository(StudentModel)

   def list_students(self) -> list[StudentModel]:
      return self.repo.list_students()
   
   def get_student(self, student_id: int) -> StudentModel | None:
      """Fetch a student by its ID."""
      return self.repo.get_student_by_id(student_id)
   
   def create(self, student: StudentModel) -> int:
      """Create a new student."""
      return self.repo.create(student)
   
   def update(self, student: StudentModel) -> int:
      """Update an existing student."""
      return self.repo.update(student)
   
   def delete(self, student_id: int) -> int:
      """Delete a student by its ID."""
      return self.repo.delete(student_id)
