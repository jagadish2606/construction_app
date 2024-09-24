# import os
# from dotenv import load_dotenv

# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")
import os
from dotenv import load_dotenv

load_dotenv()

# Code running environment
ENVIRONMENT = os.getenv("ENVIRONMENT")

# Global database URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Model generation file name
MODEL_GEN_FILE_NAME = os.getenv("MODEL_GEN_FILE_NAME")

# Debugging statements
print(f"ENVIRONMENT: {ENVIRONMENT}")
print(f"DATABASE_URL: {DATABASE_URL}")
print(f"MODEL_GEN_FILE_NAME: {MODEL_GEN_FILE_NAME}")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the .env file")
