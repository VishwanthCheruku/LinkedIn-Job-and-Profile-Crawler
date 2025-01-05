from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Database configuration
DATABASE_URL = "postgresql://user:password@localhost:5432/job_profile_db"

def setup_database():
    # Create a new database engine
    engine = create_engine(DATABASE_URL)

    # Create all tables in the database which are defined by Base's subclasses
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    return session

if __name__ == "__main__":
    session = setup_database()
    print("Database setup complete.")