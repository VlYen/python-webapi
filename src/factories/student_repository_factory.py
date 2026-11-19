import logging
from common.config import Settings, get_settings
from factories.connection_factory import ConnectionFactory
from repositories.StudentRepository import StudentRepository
from repositories.SqlLiteStudentRepository import SqlLiteStudentRepository

logger = logging.getLogger(__name__)

settings = get_settings()

class StudentRepositoryFactory:
    @staticmethod
    def create() -> StudentRepository:
        """Create and return an instance of StudentRepository based on the configured database type."""
        logger.debug(f"Creating StudentRepository for DB_TYPE: {settings.DB_TYPE}")

        studentRepository : StudentRepository = None
        # my_list = ["sqlserver", "sqlite"]
        my_list = ["sqlite"]

        if settings.DB_TYPE in my_list:
            logger.debug(f"Found '{settings.DB_TYPE}' in my_list")
            
            connection = ConnectionFactory.get_connection()

            if settings.DB_TYPE == "sqlite":
                studentRepository = SqlLiteStudentRepository(connection)

            return studentRepository

        else:
            logger.error(f"Unsupported database type: {settings.DB_TYPE}")
            raise ValueError(f"Unsupported database type: {settings.DB_TYPE}")

