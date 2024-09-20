from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Database connection
engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Reflect database tables
metadata.reflect(bind=engine)

Base = declarative_base()

# Session for database transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Generate models dynamically
def generate_models():
    for table_name in metadata.tables:
        print(f"Generating model for table: {table_name}")
        type(
            table_name.capitalize(),
            (Base,),
            {
                '__tablename__': table_name,
                '__table__': metadata.tables[table_name]
            }
        )

generate_models()

# Create tables if they don't exist
Base.metadata.create_all(engine)
