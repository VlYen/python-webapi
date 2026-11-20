import logging
from fastapi import APIRouter, Depends, HTTPException, Response, status

from models.school_class_model import SchoolClassModel
from routers.student_controller import get_student_service
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
        records : list[SchoolClassModel] = service.list_classes()

        data = {
            # "app": os.getenv("APP_NAME", "N/A"),
            # "version": os.getenv("VERSION", "N/A"),
            # "datetime_iso": datetime.now().isoformat(),
            "data": records
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

#--------------------------------------------------------------------
@router.get("/{id}")
def get_school_class(
        id: int, 
        response: Response,
        service: SchoolClassService = Depends(get_classes_service)
    ):
    try:
        school_class = service.get_class(id)
        data : dict = {
            # "app": os.getenv("APP_NAME", "N/A"),
            # "version": os.getenv("VERSION", "N/A"),
            # "datetime_iso": datetime.now().isoformat(),
        }        

        if school_class:
            response.status_code = status.HTTP_200_OK
            data["class"] = school_class
            return data
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            data["error"] = "Class not found"
            return data
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        data["error"] = str(e)
        return data    

#--------------------------------------------------------------------
@router.post("")
def create(
    school_class: SchoolClassModel, 
    response: Response,
    service: SchoolClassService = Depends(get_classes_service)
    ):
    try:
        class_id = service.create(school_class)
        response.status_code = status.HTTP_201_CREATED
        return {"id": class_id}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    finally:
        pass       