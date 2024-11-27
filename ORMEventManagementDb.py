# ORMEventManagementDb.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Event(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(String)
    location = Column(String)

# Database connection
engine = create_engine('sqlite:///ORMEventManagementDb.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Dummy data for events
dummy_data = [
    {"name": "Concert", "date": "2024-12-01", "location": "Stadium"},
    {"name": "Conference", "date": "2024-12-05", "location": "Convention Center"},
    {"name": "Wedding", "date": "2024-12-10", "location": "Beach Resort"},
    {"name": "Seminar", "date": "2024-12-15", "location": "Hotel Conference Room"},
    {"name": "Workshop", "date": "2024-12-20", "location": "Community Hall"},
]

# Insert data
for data in dummy_data:
    event_entry = Event(name=data["name"], date=data["date"], location=data["location"])
    session.add(event_entry)
session.commit()

# CRUD operations
events = session.query(Event).all()
for event in events:
    print(f"Event: {event.name}, Date: {event.date}, Location: {event.location}")

# Close session
session.close()
