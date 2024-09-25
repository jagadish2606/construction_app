from construction_app.core.database.model_generator.create_models_from_db import generate_sqlmodels
from construction_app.core.config import DATABASE_URL, MODEL_GEN_FILE_NAME



if __name__ == '__main__':
    try:
        # Test model generation
        generate_sqlmodels(db_url=DATABASE_URL, file_name=MODEL_GEN_FILE_NAME)
        print("Model generation completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


