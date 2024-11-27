# ORMJobBoardDb.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import declarative_base
Base = declarative_base()


class Job(Base):
    __tablename__ = 'jobs'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    company = Column(String)

# Database connection
engine = create_engine('sqlite:///ORMJobBoardDb.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Dummy data for jobs
dummy_data = [
    {"title": "Software Engineer", "description": "Develop software", "company": "Tech Corp"},
    {"title": "Data Scientist", "description": "Analyze data", "company": "Data Corp"},
    {"title": "Web Developer", "description": "Build websites", "company": "Web Solutions"},
    {"title": "Project Manager", "description": "Manage projects", "company": "Tech Corp"},
    {"title": "HR Specialist", "description": "Handle HR tasks", "company": "HR Corp"},
]

# Insert data
for data in dummy_data:
    job_entry = Job(title=data["title"], description=data["description"], company=data["company"])
    session.add(job_entry)
session.commit()

# CRUD operations
jobs = session.query(Job).all()
for job in jobs:
    print(f"Job Title: {job.title}, Company: {job.company}")

# Close session
session.close()
