from sqlalchemy import (Column, ForeignKey, Integer, String, create_engine)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, Mapped, mapped_column
from models import engine
Session = sessionmaker(bind = engine)
session = Session()

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True

    id = Column(Integer, primary_key = True)

# class Address(BaseModel):
#     __tablename__ = "addresses"

#     city = Column(String)
#     state = Column(String)
#     zip_code = Column(Integer)
#     user_id = Column(ForeignKey("members.id"))

#     def __repr__(self):
#         return f"<Address(id = {self.id}, city = {self.city})>"

# class Member(BaseModel):
#     __tablename__ = "members"

#     name = Column(String)
#     age = Column(Integer)
#     addresses = relationship(Address)

#     def __repr__(self):
#         return f"<Member(id = {self.id}, username = {self.name})>"

# 除了上面的寫法，我們也可以改以下面的表示方式
# back_populates 引數用於指定關係的反向關係，即關係的另一側。
# 這個參數通常用於雙向關係的設定，以確保在兩個關聯的表之間建立正確的關聯
# class Address(BaseModel):
#     __tablename__ = "addresses"

#     city = Column(String)
#     state = Column(String)
#     zip_code = Column(Integer)
#     user_id = Column(ForeignKey("members.id"))
#     user = relationship("User", back_populates = "addresses")

#     def __repr__(self):
#         return f"<Address(id = {self.id}, city = {self.city})>"

# class Member(BaseModel):
#     __tablename__ = "members"

#     name = Column(String)
#     age = Column(Integer)
#     addresses = relationship(Address)

#     def __repr__(self):
#         return f"<Member(id = {self.id}, username = {self.name})>"
    
# 我們也可以使用 Mapped 
class Address(BaseModel):
    __tablename__ = "addresses"

    city = Column(String)
    state: Mapped[str] = mapped_column()
    zip_code: Mapped[int] = mapped_column()
    member_id: Mapped[int] = mapped_column(ForeignKey("members.id"))
    member: Mapped['Member'] = relationship(back_populates = "addresses")

    def __repr__(self):
        return f"<Address(id = {self.id}, city = {self.city})>"

class Member(BaseModel):
    __tablename__ = "members"

    name = Column(String)
    age = Column(Integer)
    addresses: Mapped[list["Address"]] = relationship()

    def __repr__(self):
        return f"<Member(id = {self.id}, username = {self.name})>"

Base.metadata.create_all(engine)