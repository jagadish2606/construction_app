# import os
# from dotenv import load_dotenv

# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")

import os
from dotenv import load_dotenv
from os import getenv

load_dotenv()

# code running envirnment
ENVIRONMENT = getenv("ENVIRONMENT")

# global database URL
DATABASE_URL = getenv("DATABASE_URL")

# model_gen_file_name
MODEL_GEN_FILE_NAME = getenv("MODEL_GEN_FILE_NAME")