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
    
# 允許未映射的屬性
# class Merchant(Base):
#     __tablename__ = "merchants"
#     __allow_unmapped__ = True

#     id = Column(Integer, primary_key = True)
#     merchantname = Column(String)
#     following_id = Column(Integer, ForeignKey('merchants.id'))
#     following = relationship('Merchant', remote_side=[id], uselist= True)

#     def __repr__(self):
#         return f"<Merchant(id={self.id}, merchantname={self.merchantname}, following={self.following})>"

# 建立 Associate Table
class FollowingAssociation(BaseModel):
    __tablename__ = "following_association"

    merchant_id = Column(Integer, ForeignKey('merchants.id'))
    following_id = Column(Integer, ForeignKey('merchants.id'))

class Merchant(BaseModel):
    __tablename__ = "merchants"
    merchantname = Column(String)
    following = relationship('Merchant', secondary="following_association",
                             primaryjoin=("FollowingAssociation.merchant_id == Merchant.id"),
                             secondaryjoin=("FollowingAssociation.following_id == Merchant.id"))

    def __repr__(self):
        return f"<Merchant(id={self.id}, merchantname={self.merchantname}, following={self.following})>"

Base.metadata.create_all(engine)