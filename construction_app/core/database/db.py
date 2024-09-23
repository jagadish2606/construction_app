# import os
# from sqlalchemy import create_engine, MetaData
# from databases import Database
# from dotenv import load_dotenv

# # Load environment variables from the .env file
# load_dotenv()

# # Get the DATABASE_URL from .env
# DATABASE_URL = os.getenv("DATABASE_URL")

# # Create the SQLAlchemy engine
# engine = create_engine(DATABASE_URL)
# metadata = MetaData()

# # Create the async database connection using the 'databases' package
# database = Database(DATABASE_URL)


from sqlmodel import create_engine, Session
from sqlalchemy.pool import NullPool
from core.config.config import DATABASE_URL

def get_db():
    engine = create_engine(DATABASE_URL, pool_pre_ping=True, poolclass=NullPool)
    try:
        db = Session(bind=engine, autoflush=False)
        yield db
    finally:
        db.close()
