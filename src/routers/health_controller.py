import logging
import os
from datetime import datetime
import json
from fastapi import APIRouter, Response, status
import pyodbc

router = APIRouter()
logger = logging.getLogger(__name__)

#--------------------------------------------------------------------
@router.get("")
def health(response: Response):
    try:
        logger.info("Health check endpoint called")
        data = {
            "app": os.getenv("APP_NAME", "N/A"),
            "version": os.getenv("VERSION", "N/A"),
            "datetime_iso": datetime.now().isoformat()
        }
        print(pyodbc.drivers())

        response.status_code = status.HTTP_200_OK  # Set the desired HTTP status code
        response.media_type = "application/json"
        return data
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR  # Set the desired HTTP status code
        return {"error": str(e)}          

