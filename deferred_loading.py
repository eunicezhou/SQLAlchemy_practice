from sqlalchemy import (Column, String, create_engine, select)
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column, deferred, undefer
from models import engine

Session = sessionmaker(bind = engine)
session = Session()

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key= True)

class UserLegacy(Base):
    __tablename__ = 'userlegacies'

    id: Mapped[int] = mapped_column(primary_key = True)
    nickname: Mapped[str] = deferred(mapped_column(String))
    first_name: Mapped[str] = mapped_column(String)
    last_name = deferred(Column(String))
    other_value: Mapped[str] = mapped_column(String, deferred = True)

    def __repr__(self) -> str:
        return f"<UserLegacy: {self.id} - {self.nickname}>"
    
Base.metadata.create_all(engine)

# session.add(
#     UserLegacy(
#         first_name = "Zeq",
#         last_name = "Tech",
#         nickname = "ZeqTech",
#         other_value = "other"
#     )
# )
# session.commit()

# 下面三種都是查詢方式
# user = session.scalar(select(UserLegacy))
# user = session.execute(select(UserLegacy)).scalar()
# user = session.query(UserLegacy).first()
# print(user)
# print(user.first_name)
# print(user.last_name)
# print(user.other_value)
 
other_user = session.query(UserLegacy).options(undefer(UserLegacy.first_name), undefer(UserLegacy.last_name), undefer(UserLegacy.other_value)).first()
print(other_user)
print(other_user.first_name)
print(other_user.last_name)
print(other_user.other_value)