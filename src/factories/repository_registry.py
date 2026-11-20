from functools import lru_cache

from factories.RepositoryFactory import RepositoryFactory
from factories.connection_factory import ConnectionFactory
from repositories.SqlLiteSchoolClassRepository import SqlLiteSchoolClassRepository
from repositories.SqlLiteStudentRepository import SqlLiteStudentRepository
from models.school_class_model import SchoolClassModel
from models.student_model import StudentModel


@lru_cache
def get_repository_factory() -> RepositoryFactory:
    """Provides a cached instance of RepositoryFactory with registered repositories."""
    factory = RepositoryFactory()
    factory.register(
        SchoolClassModel,
        lambda: SqlLiteSchoolClassRepository(ConnectionFactory.get_connection())
    )
    factory.register(
        StudentModel,
        lambda: SqlLiteStudentRepository(ConnectionFactory.get_connection())
    )
    return factory