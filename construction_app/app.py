from fastapi import FastAPI
import os
from dotenv import load_dotenv
from construction_app.endpoints.user import router as user_router

from construction_app.core.config import ENVIRONMENT, DATABASE_URL
from construction_app.models import models
load_dotenv()

app = FastAPI()

# ENVIRONMENT = os.getenv("ENVIRONMENT")
# DATABASE_URL = os.getenv("DATABASE_URL")
# MODEL_GEN_FILE_NAME = os.getenv("MODEL_GEN_FILE_NAME")
# Include your endpoints
app.include_router(user_router, prefix='/users')
