from functools import lru_cache

from factories.RepositoryFactory import RepositoryFactory
from factories.school_class_repository_factory import SchoolClassRepositoryFactory
from factories.student_repository_factory import StudentRepositoryFactory
from models.school_class_model import SchoolClassModel
from models.student_model import StudentModel


@lru_cache
def get_repository_factory() -> RepositoryFactory:
    factory = RepositoryFactory()
    factory.register(SchoolClassModel, SchoolClassRepositoryFactory.create)
    factory.register(StudentModel, StudentRepositoryFactory.create)
    return factory