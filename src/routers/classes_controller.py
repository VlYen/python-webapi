import logging
from fastapi import APIRouter, Depends, HTTPException, Response, status

from models.school_class_model import SchoolClassModel
from services.school_class_service import SchoolClassService
from factories.repository_registry import get_repository_factory

router = APIRouter()
logger = logging.getLogger(__name__)

#--------------------------------------------------------------------
def get_classes_service() -> SchoolClassService:
    """Dependency function to provide a SchoolClassService instance."""
    factory = get_repository_factory()
    try:
        return SchoolClassService(factory)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc))

#--------------------------------------------------------------------
@router.get("")
async def get_available_classes(
    response: Response,
    service: SchoolClassService = Depends(get_classes_service)
    ):
    try:
        # classes : list[SchoolClassModel] = service.list_classes()

        data = {
            # "app": os.getenv("APP_NAME", "N/A"),
            # "version": os.getenv("VERSION", "N/A"),
            # "datetime_iso": datetime.now().isoformat(),
            "data": service.list_classes()
        }

        response.status_code = status.HTTP_200_OK  # Set the desired HTTP status code
        response.media_type = "application/json"
        return data
    except Exception as e:
        logger.error(f"Error occurred while getting available classes: {str(e)}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR  # Set the desired HTTP status code        
        return {"error": str(e)}          
    finally:
        pass