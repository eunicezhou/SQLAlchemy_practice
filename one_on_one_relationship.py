from sqlalchemy import (Column, ForeignKey, Integer, String, create_engine)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from models import engine

Session = sessionmaker(bind = engine)
session = Session()

Base = declarative_base()

class Email(Base):
    __tablename__ = "emails"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey("people.id"))
    user = relationship("Person", back_populates = "email")

class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = relationship("Email", back_populates="user", uselist=False)

# Base.metadata.create_all(engine)

person1 = Person(name="John Doe")
email_1 = Email(email = "johndoe@example.com", user = person1)
# session.add(person1)
# session.add(email_1)
# session.commit()

print(person1.name)
print(email_1.email)
print(person1.email.email)
print(email_1.user.name)