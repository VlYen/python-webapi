import logging
from common.config import Settings, get_settings
from factories.connection_factory import ConnectionFactory
from repositories.SchoolClassRepository import SchoolClassRepository
from repositories.SqlLiteSchoolClassRepository import SqlLiteSchoolClassRepository

logger = logging.getLogger(__name__)

settings = get_settings()

class SchoolClassRepositoryFactory:
    @staticmethod
    def create() -> SchoolClassRepository:
        """Create and return an instance of SchoolClassRepository based on the configured database type."""
        logger.debug(f"Creating SchoolClassRepository for DB_TYPE: {settings.DB_TYPE}")

        schoolClassRepository : SchoolClassRepository = None
        # my_list = ["sqlserver", "sqlite"]
        my_list = ["sqlite"]

        if settings.DB_TYPE in my_list:
            logger.debug(f"Found '{settings.DB_TYPE}' in my_list")
            
            connection = ConnectionFactory.get_connection()

            if settings.DB_TYPE == "sqlite":
                schoolClassRepository = SqlLiteSchoolClassRepository(connection)

            return schoolClassRepository

        else:
            logger.error(f"Unsupported database type: {settings.DB_TYPE}")
            raise ValueError(f"Unsupported database type: {settings.DB_TYPE}")

