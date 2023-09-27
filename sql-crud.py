import os
from dotenv import load_dotenv

from sqlalchemy import (
    create_engine, Column, Integer, String
  )

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

db_url = f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}"

db = create_engine(db_url)

base = declarative_base()


# create a class-based model for the Programmer table
class Programmer(base):
  __tablename__ = "Programmer"
  id = Column(Integer, primary_key=True)
  first_name = Column(String)
  last_name = Column(String)
  gender = Column(String)
  nationality = Column(String)
  famous_for = Column(String)


# create a session maker bound to our db
Session = sessionmaker(db)

# create a session
session = Session()

# create the db using the declarative base class
base.metadata.create_all(db)

# create a new programmer
ada_lovelace = Programmer(
  first_name = "Ada",
  last_name = "Lovelace",
  gender = "Female",
  nationality = "British",
  famous_for = "First Computer Programmer"
)

alan_turing = Programmer(
  first_name = "Alan",
  last_name = "Turing",
  gender = "Male",
  nationality = "British",
  famous_for = "Modern Computing"
)

grace_hopper = Programmer(
  first_name = "Grace",
  last_name = "Hopper",
  gender = "Female",
  nationality = "American",
  famous_for = "COBOL Language"
)

margaret_hamilton = Programmer(
  first_name = "Margaret",
  last_name = "Hamilton",
  gender="Female",
  nationality="American",
  famous_for="Apollo 11"
)

bill_gates = Programmer(
  first_name = "Bill",
  last_name = "Gates",
  gender="Male",
  nationality="American",
  famous_for="Microsoft founder"
)

tim_berners_lee = Programmer(
  first_name = "Tim",
  last_name = "Berners Lee",
  gender="Male",
  nationality="British",
  famous_for="World Wide Web"
)

stephen_dawson = Programmer(
  first_name="Stephen",
  last_name="Dawson",
  gender="Male",
  nationality="Irish",
  famous_for="Being"
)

# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(stephen_dawson)




# update a single record query
# programmer = session.query(Programmer).filter_by(id=7).first()

# programmer.famous_for = "Being multilingual"

# people = session.query(Programmer)
# for person in people:
#   if person.gender == "Female":
#     person.gender = "F"
#   else:
#     person.gender = "M"

# deleting a record
# fname = input("Enter first name: ")
# lname = input("Enter last name: ")

# programmer = session.query(Programmer).filter_by(first_name=fname, last_name=lname).first()

# if programmer is not None:
#   print(f"Found programmer: {programmer.first_name} {programmer.last_name}")
#   confirmation = input("Are you sure you want to delete this record? (y/n) ")
#   if confirmation.lower() == "y":
#     session.delete(programmer)
#     session.commit()
#     print("Programmer has been deleted.")
#   else:
#     print("Programmer not deleted.")
# else:
#   print("No records found.")

# commit the record the database
# session.commit()

programmers = session.query(Programmer)
for programmer in programmers:
  print(
    programmer.id,
    programmer.first_name + " " + programmer.last_name,
    programmer.gender,
    programmer.nationality,
    programmer.famous_for,
    sep=" | "
    )