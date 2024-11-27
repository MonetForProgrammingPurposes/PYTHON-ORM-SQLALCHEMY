from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base for our model
Base = declarative_base()

# Define the Product class representing the products table
class Product(Base):
    __tablename__ = 'products'
    
    # Columns for the products table
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)  # Ensure names are unique
    price = Column(Integer)

# Create the database engine and connect to the SQLite database
engine = create_engine('sqlite:///ORMEcommerceDb.db', echo=True)

# Create all tables based on the model (products table will be created if it doesn't exist)
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Define dummy data for products
dummy_data = [
    {"name": "Laptop", "price": 1000},
    {"name": "Phone", "price": 500},
    {"name": "Headphones", "price": 200},
    {"name": "Keyboard", "price": 50},
    {"name": "Mouse", "price": 25},
]

try:
    # Loop over the dummy data and insert if not already in the database
    for data in dummy_data:
        # Check if product already exists by name
        existing_product = session.query(Product).filter_by(name=data["name"]).first()
        
        if not existing_product:  # If product doesn't exist, insert
            product_entry = Product(name=data["name"], price=data["price"])
            session.add(product_entry)  # Add the product to the session
            print(f"Inserting: {data['name']}")
        else:
            print(f"Product already exists: {data['name']}")  # Skip duplicate
    
    # Commit the changes to the database after all products are processed
    session.commit()
    print("Changes committed successfully.")



finally:
    # Query to check if data was inserted correctly
    products = session.query(Product).all()
    print("\nProducts in Database:")
    for product in products:
        print(f"Product: {product.name}, Price: {product.price}")

   
