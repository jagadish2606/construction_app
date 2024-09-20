from sqlalchemy.orm import Session
from ..models import engine

def get_all_users(db: Session):
    # Query users from the database (adjust this based on your table structure)
    return db.query(engine.metadata.tables['users']).all()
