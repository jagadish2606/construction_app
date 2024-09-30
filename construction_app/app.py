from fastapi import FastAPI
import os
from dotenv import load_dotenv
from construction_app.endpoints.user import router as user_router

from construction_app.core.config import ENVIRONMENT, DATABASE_URL
from fastapi.middleware.cors import CORSMiddleware
from construction_app.models import models
load_dotenv()

app = FastAPI()

# ENVIRONMENT = os.getenv("ENVIRONMENT")
# DATABASE_URL = os.getenv("DATABASE_URL")
# MODEL_GEN_FILE_NAME = os.getenv("MODEL_GEN_FILE_NAME")
# Include your endpoints


# Allow CORS for your frontend URL
origins = [
    "http://localhost:5173",  # React app running on this port
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow these origins to access the backend
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (POST, GET, etc.)
    allow_headers=["*"],  # Allow all headers
)
app.include_router(user_router, prefix='/users')
