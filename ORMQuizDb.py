# ORMQuizDb.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the base class
Base = declarative_base()

# Define the Quiz model
class Quiz(Base):
    __tablename__ = 'quiz'  # Name of the table in the database

    id = Column(Integer, primary_key=True)  # Primary key column
    question = Column(String)  # Column for question
    answer = Column(String)    # Column for answer

# Create the SQLite engine for ORMQuizDb.db
engine = create_engine('sqlite:///ORMQuizDb.db', echo=True)

# Create the table in the database if it does not exist
Base.metadata.create_all(engine)

# Set up the session
Session = sessionmaker(bind=engine)
session = Session()

# Dummy data for the quiz
dummy_data = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "Who wrote Hamlet?", "answer": "Shakespeare"},
    {"question": "What is the boiling point of water?", "answer": "100°C"},
    {"question": "What is the speed of light?", "answer": "299,792,458 m/s"},
]

# Insert the dummy data into the quiz table
for data in dummy_data:
    quiz_entry = Quiz(question=data["question"], answer=data["answer"])
    session.add(quiz_entry)

# Commit the changes to the database
session.commit()

# Perform CRUD operations: Read all quizzes
quizzes = session.query(Quiz).all()
for quiz in quizzes:
    print(f"Question: {quiz.question}, Answer: {quiz.answer}")

# Update the first quiz's answer
quiz_to_update = session.query(Quiz).filter_by(id=1).first()
if quiz_to_update:
    quiz_to_update.answer = "London"  # Change the answer
    session.commit()

# Delete the second quiz
quiz_to_delete = session.query(Quiz).filter_by(id=2).first()
if quiz_to_delete:
    session.delete(quiz_to_delete)
    session.commit()

# Close the session
session.close()
