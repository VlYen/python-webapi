import os
import logging
from repositories.StudentRepository import StudentRepository
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException, Response, status

from models.student_model import StudentModel
from services.student_service import StudentService
from models.student_model import StudentModel
from factories.student_repository_factory import StudentRepositoryFactory

router = APIRouter()
logger = logging.getLogger(__name__)

#--------------------------------------------------------------------
def get_student_service() -> StudentService:
    """Dependency function to provide a StudentService instance."""
    try:
        repo = StudentRepositoryFactory.create()
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(exc))
    return StudentService(repo)

#--------------------------------------------------------------------
@router.get("")
async def get_students(
    response: Response,
    service: StudentService = Depends(get_student_service)
    ):
    try:
        students : list[StudentModel] = service.list_students()

        data = {
            # "app": os.getenv("APP_NAME", "N/A"),
            # "version": os.getenv("VERSION", "N/A"),
            # "datetime_iso": datetime.now().isoformat(),
            "data": students
        }

        response.status_code = status.HTTP_200_OK  # Set the desired HTTP status code
        response.media_type = "application/json"
        return data
    except Exception as e:
        logger.error(f"Error occurred while getting students: {str(e)}")
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR  # Set the desired HTTP status code        
        return {"error": str(e)}          
    finally:
        pass

#--------------------------------------------------------------------
@router.get("/{student_id}")
def get_student(
        student_id: int, 
        response: Response,
        service: StudentService = Depends(get_student_service)
    ):
    try:
        student = service.get_student(student_id)
        data : dict = {
            # "app": os.getenv("APP_NAME", "N/A"),
            # "version": os.getenv("VERSION", "N/A"),
            # "datetime_iso": datetime.now().isoformat(),
        }        

        if student:
            response.status_code = status.HTTP_200_OK
            data["student"] = student
            return data
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            data["error"] = "Student not found"
            return data
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        data["error"] = str(e)
        return data

#--------------------------------------------------------------------
@router.post("")
def create(
    student: StudentModel, 
    response: Response,
    service: StudentService = Depends(get_student_service)
    ):
    try:
        student_id = service.create(student)
        response.status_code = status.HTTP_201_CREATED
        return {"id": student_id}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    finally:
        pass        

#--------------------------------------------------------------------
@router.put("")
def update(
    student: StudentModel, 
    response: Response,
    service: StudentService = Depends(get_student_service)
    ):
    try:
        rows_updated = service.update(student)
        if rows_updated > 0:
            response.status_code = status.HTTP_200_OK
            return {"message": "Student updated successfully"}
        else:
            response.status_code = status.HTTP_404_NOT_FOUND
            return {"error": "Student not found"}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    finally:
        pass 

#--------------------------------------------------------------------
@router.delete("/{student_id}")
def delete(
   student_id: int, 
   response: Response,
   service: StudentService = Depends(get_student_service)
   ):
   try:
      rows_deleted = service.delete(student_id)
      if rows_deleted > 0:
         response.status_code = status.HTTP_200_OK
         return {"message": "Student deleted successfully"}
      else:
         response.status_code = status.HTTP_404_NOT_FOUND
         return {"error": "Student not found"}
   except Exception as e:
      response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
      return {"error": str(e)}
   finally:
      pass