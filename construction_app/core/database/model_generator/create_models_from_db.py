import sys
from sqlmodel import create_engine, MetaData
from sqlacodegen_v2.generators import SQLModelGenerator, TablesGenerator

def get_engine(db_url):
    """Create and return the engine instance."""
    return create_engine(db_url)

def get_metadata(engine):
    """Create and return the metadata instance."""
    metadata = MetaData()
    metadata.reflect(engine)  # Removed `bind` parameter
    return metadata

def get_engine_metadata(db_url):
    """Create and return engine and metadata instance."""
    engine = get_engine(db_url)
    metadata = get_metadata(engine)
    return engine, metadata

def generate_sqlmodels(db_url, file_name):
    """Generate SQLModel models and write to a file."""
    engine, metadata = get_engine_metadata(db_url=db_url)

    generator = SQLModelGenerator(metadata=metadata, bind=engine, options=[])
    models = generator.generate()

    # Write generated models to the specified file
    with open(file_name, 'w') as file:
        file.write(models)

def generate_sqla_models(db_url, file_name):
    """Generate models conforming to SQLAlchemy."""
    engine, metadata = get_engine_metadata(db_url=db_url)
    
    generator = TablesGenerator(metadata=metadata, bind=engine, options=[])
    models = generator.generate_models()
    rendered_models = generator.rendered_models(models)
    
    # Write generated models to the specified file
    with open(file_name, 'w') as file:
        file.write(rendered_models)
