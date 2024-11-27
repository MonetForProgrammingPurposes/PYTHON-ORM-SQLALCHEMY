# ORMTravelBookingDb.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Booking(Base):
    __tablename__ = 'bookings'
    
    id = Column(Integer, primary_key=True)
    destination = Column(String)
    customer_name = Column(String)
    date = Column(String)

# Database connection
engine = create_engine('sqlite:///ORMTravelBookingDb.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Dummy data for bookings
dummy_data = [
    {"destination": "Paris", "customer_name": "John Doe", "date": "2024-12-05"},
    {"destination": "London", "customer_name": "Jane Smith", "date": "2024-12-12"},
    {"destination": "Rome", "customer_name": "Bob Johnson", "date": "2024-12-20"},
    {"destination": "Tokyo", "customer_name": "Alice Brown", "date": "2024-12-25"},
    {"destination": "New York", "customer_name": "Charlie Davis", "date": "2024-12-30"},
]

# Insert data
for data in dummy_data:
    booking_entry = Booking(destination=data["destination"], customer_name=data["customer_name"], date=data["date"])
    session.add(booking_entry)
session.commit()

# CRUD operations
bookings = session.query(Booking).all()
for booking in bookings:
    print(f"Booking: {booking.destination}, Customer: {booking.customer_name}, Date: {booking.date}")

# Close session
session.close()
