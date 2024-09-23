# from sqlalchemy import create_engine, MetaData
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL")

# # Database connection
# engine = create_engine(DATABASE_URL)
# metadata = MetaData()

# # Reflect database tables
# metadata.reflect(bind=engine)

# Base = declarative_base()

# # Session for database transactions
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Generate models dynamically
# def generate_models():
#     for table_name in metadata.tables:
#         print(f"Generating model for table: {table_name}")
#         type(
#             table_name.capitalize(),
#             (Base,),
#             {
#                 '__tablename__': table_name,
#                 '__table__': metadata.tables[table_name]
#             }
#         )

# generate_models()

# # Create tables if they don't exist
# Base.metadata.create_all(engine)


from construction_app.core.database.model_generator.create_models_from_db import generate_sqlmodels
from construction_app.core.config import DATABASE_URL, MODEL_GEN_FILE_NAME



if __name__ == '__main__':
    try:
        # Test model generation
        generate_sqlmodels(db_url=DATABASE_URL, file_name=MODEL_GEN_FILE_NAME)
        print("Model generation completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


