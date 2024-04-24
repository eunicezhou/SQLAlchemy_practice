from sqlalchemy import (Column, ForeignKey, Integer, String, create_engine, Table)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from models import engine

Session = sessionmaker(bind = engine)
session = Session()

Base = declarative_base()

# Association Table
# student_course_link = Table('student_course', Base.metadata,
#                             Column('student_id', Integer, ForeignKey('student.id')),
#                             Column('course_id', Integer, ForeignKey('courses.id')))
# 上面的寫法也可以使用 class 來建構
class StudentCourse(Base):
    __tablename__ = 'student_course_link'
    id = Column(Integer, primary_key=True)
    student_id = Column('student_id', Integer, ForeignKey('students.id'))
    course_id = Column('course_id', Integer, ForeignKey('courses.id'))

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    courses = relationship("Course", secondary='student_course_link', back_populates='students')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    students = relationship("Student", secondary='student_course_link', back_populates='courses')

Base.metadata.create_all(engine)

# math = Course(title = "Mathematics")
# physics = Course(title = "Physics")
# english = Course(title = "English")
# chinese = Course(title = "Chinese")

# bill = Student(name = 'Bill', courses = [math, physics])
# mary = Student(name = 'Mary', courses = [math])
# bob = Student(name = 'Bob', courses = [english, math, physics])
# vic = Student(name = 'Vic', courses = [chinese, physics])

# session.add_all([english, chinese, bob, vic])
# session.commit()

mary = session.query(Student).filter_by(name = "Mary").first()
courses = [course.title for course in mary.courses]
print(f"Mary's Courses: {', '.join(courses)}")

# 如果是單個表格中的紀錄之間的多對多關係，則可以使用 follow
class FansAssociation(Base):
    __tablename__ = 'fans_associations'
    id = Column(Integer, primary_key= True)

    follower_id = Column(Integer, ForeignKey('fans.id'))
    following_id = Column(Integer, ForeignKey('fans.id'))

class Fan(Base):
    __tablename__ = 'fans'
    id = Column(Integer, primary_key= True)
    name = Column(String, nullable= False)

    following = relationship(
        "Fan",
        secondary="fans_associations",
        primaryjoin="FansAssociation.follower_id == Fan.id",
        secondaryjoin="FansAssociation.following_id == Fan.id",
        backref='followers'
    )

    def __repr__(self):
        return f"<Fan: {self.name}>"
    
Base.metadata.create_all(engine)

fan_1 = Fan(name = "Mary")
fan_2 = Fan(name = "Bob")
fan_3 = Fan(name = "Kitty")

fan_1.following.append(fan_2)
fan_2.following.append(fan_1)
fan_3.following.append(fan_1)

session.add_all([fan_1, fan_2, fan_3])
session.commit()

print(f"{fan_1} is following: {fan_1.following}")
print(f"{fan_1} is being followed by: {fan_1.followers}")