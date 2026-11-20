import logging
from factories.RepositoryFactory import RepositoryFactory
from models.school_class_model import SchoolClassModel

logger = logging.getLogger(__name__)

class SchoolClassService:
   def __init__(self, factory: RepositoryFactory):
      self.repo = factory.get_repository(SchoolClassModel)

   def list_classes(self) -> list[SchoolClassModel]:
      return self.repo.list()

   def get_class(self, class_id: int) -> SchoolClassModel | None:
      """Fetch a class by its ID."""
      return self.repo.get_by_id(class_id)

   def create(self, school_class: SchoolClassModel) -> int:
      """Create a new class."""
      return self.repo.create(school_class)

   def update(self, school_class: SchoolClassModel) -> int:
      """Update an existing class."""
      return self.repo.update(school_class)

   def delete(self, class_id: int) -> int:
      """Delete a class by its ID."""
      return self.repo.delete(class_id)
