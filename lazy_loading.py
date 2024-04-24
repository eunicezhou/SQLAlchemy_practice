from sqlalchemy import (Column, ForeignKey, Integer, String, create_engine, Table, Text)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, joinedload
from models import engine
from time import perf_counter

Session = sessionmaker(bind = engine)
session = Session()

Base = declarative_base()

class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # posts = relationship('Post', lazy='select', backref='teacher')
    # posts = relationship('Post', lazy='selectin', backref='teacher')
    # latest_post = relationship('Post', uselist = False, lazy= 'joined')
    # sensitive_informations = relationship('SensitiveInformation', backref = 'teacher', lazy = 'raise')
    # posts = relationship('Post', backref = 'teacher', lazy = 'subquery')
    # posts = relationship('Post', backref = 'teacher', lazy = 'write_only')
    posts = relationship('Post', backref = 'teacher', lazy = 'dynamic')

    def __repr__(self):
        return f"<Teacher {self.name}>"

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key= True)
    content = Column(Text)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    def __repr__(self):
        return f"<Post {self.id}>"
    
class SensitiveInformation(Base):
    __tablename__ = 'sensitive_informations'
    id = Column(Integer, primary_key= True)
    content = Column(Text)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))

    def __repr__(self):
        return f"<SensitiveInformation {self.id}>"

Base.metadata.create_all(engine)

# teacher1 = Teacher(
#     name = "Monica",
#     posts = [
#         Post(content = f"This is the content for {x}")
#         for x in range(1, 5)
#     ]
# )
# session.add(teacher1)

# teacher1 = session.query(Teacher).first()
# print(teacher1)
# print(f"Accessing Posts specifically: {teacher1.posts}")

# 這邊舉例 lazy = select 可能會遇到的問題
# 每建立一個 Teacher 就會建立 5 個留言
# 由於 Teacher 中的 posts 屬性的 lazy = select，因此每抓出一個老師就會將留言加載一次
# session.add_all(
#     [
#         Teacher(
#             name = f"Teacher{y}",
#             posts =[
#                 Post(content = f"This is the latest content for {y * 5 + x}")
#                 for x in range(5)
#             ]
#         ) for y in range(1000,1010)
#     ]
# )
# session.commit()
# print('\n Accessing All Teachers Posts')
# start = perf_counter()
# teachers = session.query(Teacher).all()
# for teacher in teachers:
#     print(teacher.posts)
# print(f"Done in: {perf_counter() - start}")

# 下面為 lazy = joined 時的資料建構範例
# session.add_all(
#     [
#         Teacher(
#             name = f"Teacher{y}",
#             latest_post =Post(content = f"This is the latest content for {y}")
#         ) for y in range(1000,1010)
#     ]
# )
# session.commit()
# teachers = session.query(Teacher).all()
# for teacher in teachers:
#     print(teacher.name, teacher.latest_post.content)

# 下面為 lazy = raise 時建構資料的範例
# session.add_all(
#     [
#         Teacher(
#             name = f"Teacher{y}",
#             sensitive_informations = [
#                 SensitiveInformation(
#                     content = f"This is a sensitive information for Teacher{y}"
#                 )
#             ]
#         )for y in range(10)
#     ]
# )
# session.commit()
# teachers = session.query(Teacher).options(joinedload(Teacher.sensitive_informations)).all()
# for teacher in teachers:
#     print(teacher.name)
#     try:
#         for information in teacher.sensitive_informations:
#             print(information.content)
#     except Exception as e:
#         print("SensitiveInformation cannot be accessed directly:", e)

# 下面為使用 lazy = subquery 建立資料的寫法
# session.add_all(
#     [
#         Teacher(
#             name = f"Teacher{y}",
#             posts = [
#                 Post(
#                     content = f"This is the content for {y * 5 + x}"
#                 )
#                 for x in range(5)
#             ]
#         )for y in range(10)
#     ]
# )
# session.commit()
# teachers = session.query(Teacher).all()
# for teacher in teachers:
#     print(teacher.name)
#     for post in teacher.posts:
#         print(post.content)

# 下面為使用 lazy = write_only 建立資料的方式
# teacher = session.query(Teacher).first()
# print(teacher.posts) #  lazy = write_only，表示該關係僅用於寫入。因此，當您嘗試訪問 teacher.posts 時，會出現錯誤或無效的結果
# teacher1 = session.query(Teacher).filter_by(name = "Teacher1000").first()
# new_post = Post(content = "This is a new line !!!!!")
# teacher1.posts.add(new_post) 
# session.commit()

# 下面使用 lazy = dynamic 建立資料的方式
# session.add(
#     Teacher(
#         name = "Zhen",
#         posts = [
#             Post(
#                 content = f"Content {x}"
#             )for x in range(50)
#         ]
#     )
# )
# session.commit()
teacher = session.query(Teacher).filter_by(name = "Zhen").first()
print(teacher.posts)

recent_posts = teacher.posts.order_by(Post.id.desc()).limit(10).all()
for post in recent_posts:
    print(post.content)