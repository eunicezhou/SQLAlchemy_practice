from typing import Optional
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, sessionmaker

engine = create_engine("sqlite:///12_Join_Types/data12.db")
session = sessionmaker(bind = engine)()

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key= True)

class Address(Base):
    __tablename__ = "addresses"

    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"))
    data: Mapped[str]

    def __repr__(self) -> str:
        return f"<Address: {self.data}>"
    
class User(Base):
    __tablename__ = "users"

    first_name: Mapped[str]
    last_name: Mapped[str]
    address: Mapped[Address] = relationship()

    def __repr__(self) -> str:
        return f"<User: {self.first_name} {self.last_name}>"
    
Base.metadata.create_all(engine)

# #This address IS used
# address_1 = Address(data = "1234 Random Address")

# #These addresses are NOT used
# address_2 = Address(data = "5678 Non-existant Address")
# address_3 = Address(data = "9895 Extra Address")

# # User with an address
# user_1 = User(
#     first_name = "Zeq",
#     last_name = "Tech",
#     address = address_1,
# )
# user_2 = User(
#     first_name = "Banana",
#     last_name = "Kan",
#     address = None
# )

# session.add_all([address_1, address_2, address_3, user_1, user_2])
# session.commit()

# INNER JOIN
# result = session.query(User).join(Address).all()
# print(result)
# result = session.query(User, Address).join(Address, User.id == Address.user_id).all()
# print(result)

# ANTI JOIN
# result = (
#     session.query(User, Address)
#     .join(Address, full = True)
#     .filter(User.address == None, Address.user_id == None)
#     .all()
# )
# print(result)

# Left Join || Right Join
# Return all users reguardless if they have addresses or not
result = session.query(User).outerjoin(Address).all()
print(result)
result = session.query(User).join(Address, isouter= True).all()
print(result)

# Left Outer Join || Right Outer Join
result = session.query(User).outerjoin(Address).filter(User.address == None).all()
print(result)

# Full Outer Join
left_join = session.query(User, Address).outerjoin(Address)
right_join = session.query(User, Address).outerjoin(User)
full_outer_join = left_join.union(right_join)
print(full_outer_join.all())

# This will return all rows, reguardless if there is a user associated with the Addresss
# or reguardless if there is an address associated with a user
result = session.query(User, Address).join(Address, isouter = True, full = True).all()
print(result)
