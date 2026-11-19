import os
from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from common.pretty_json_response import PrettyJSONResponse
from common.screen_utils import clear_console
from routers import (
    health_controller, 
    student_controller
)

from app_logging.logging_config import setup_logging
from app_logging.middleware import CustomValueMiddleware

load_dotenv()  # take environment variables from .env.
setup_logging()

app = FastAPI(
    title = os.getenv("APP_NAME", "N/A"),
    description = os.getenv("APP_DESCRIPTION", "N/A"),
    version = os.getenv("VERSION", "N/A"),
    default_response_class=PrettyJSONResponse
    )

# Configure CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)    

# Add custom middleware
app.add_middleware(CustomValueMiddleware)

# Add favicon endpoint to suppress 404 errors
@app.get('/favicon.ico', include_in_schema=False)
async def favicon():
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# If you want app-wide handling: 
# @app.exception_handler(ValueError)
# async def value_error_handler(request, exc):
#     return JSONResponse(
#         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#         content={"message": str(exc)}
#     )

app.include_router(health_controller.router, prefix="/health", tags=["health"])
app.include_router(student_controller.router, prefix="/students", tags=["students"])

clear_console()


