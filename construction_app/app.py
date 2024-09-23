from fastapi import FastAPI
from construction_app.endpoints import user

from construction_app.core.config import ENVIRONMENT, DATABASE_URL

app = FastAPI()

# ENVIRONMENT = os.getenv("ENVIRONMENT")
# DATABASE_URL = os.getenv("DATABASE_URL")
# MODEL_GEN_FILE_NAME = os.getenv("MODEL_GEN_FILE_NAME")
# Include your endpoints
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to Adhi Construction API"}
