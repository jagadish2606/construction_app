from dotenv import load_dotenv
import os

# Specify the explicit path to the .env file
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path=env_path)

ENVIRONMENT = os.getenv("ENVIRONMENT")
DATABASE_URL = os.getenv("DATABASE_URL")
MODEL_GEN_FILE_NAME = os.getenv("MODEL_GEN_FILE_NAME")

# print(f"ENVIRONMENT: {ENVIRONMENT}")
# print(f"DATABASE_URL: {DATABASE_URL}")
# print(f"MODEL_GEN_FILE_NAME: {MODEL_GEN_FILE_NAME}")
