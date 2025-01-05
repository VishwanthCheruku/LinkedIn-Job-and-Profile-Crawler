from sqlalchemy import create_engine, Column, String, Text, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Job(Base):
    __tablename__ = 'jobs'
    id = Column(String, primary_key=True)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    description = Column(Text)
    skills = Column(JSON)

class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(String, primary_key=True)
    name = Column(String)
    title = Column(String)
    location = Column(String)
    skills = Column(JSON)

# Database connection
DATABASE_URL = "postgresql://user:password@localhost:5432/job_profile_db"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()