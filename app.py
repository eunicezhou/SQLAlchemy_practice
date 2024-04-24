from sqlalchemy import or_, not_, func
from sqlalchemy.orm import sessionmaker
from models import User, engine
# from relationships import Address, session, Member 
from relationships import Merchant

Session = sessionmaker(bind = engine)

session = Session()

# user = User(name = "John Doe", age = 30, sex = "male")
# user_2 = User(name = "Andrew Pip", age = 28, sex = "male")
# user_3 = User(name = "Eunice Zhou", age = 27, sex = "female")
# user_4 = User(name = "Joyce Liao", age = 26, sex = "female")
# user_5 = User(name = "Iron Man", age = 57, sex = "male")
# user_6 = User(name = "Richard Rodriguez", age = 35, sex = "male")
# user_7 = User(name = "Florence Hsu", age = 60, sex = "female")


# session.add(user)
# session.add_all([user_2, user_3, user_4, user_5, user_6, user_7])
# session.commit()

# 篩選資料
# users = session.query(User).all()
# for user in users:
#     print('id:', user.id, ', name: ', user.name, ', age: ', user.age)
# john = session.query(User).filter_by(name = "John Doe").all()
# print(john)
# iron_man = session.query(User).filter_by(name = "Iron Man").one_or_none() # one_or_none() 只能回傳一筆資料，因此只能用於篩選具有獨特性的資料
# print(iron_man)

# 修改紀錄中的資料
# user_2 = session.query(User).filter_by(id = 2).first()
# user_2.name = "Jonny Jane"
# user_2.age = 25
# session.commit()

# 刪除資料
# user = session.query(User).filter_by(id = 1).first()
# session.delete(user)
# session.commit()

# 依照順序顯示資料
# users = session.query(User).order_by(User.age).all() # 從小到大排列
# for user in users:
#     print('id:', user.id, ', name: ', user.name, ', age: ', user.age)

# users = session.query(User).order_by(User.age.desc()).all() # 從大到小排列
# for user in users:
#     print('id:', user.id, ', name: ', user.name, ', age: ', user.age)

# 篩選資料
# users_obove_30 = session.query(User).filter(User.age >= 30).all()
# print(len(users_obove_30))

# jonny = session.query(User).where(User.name == "Jonny Jane").all()
# print(len(jonny))

# 篩選出 "或" 的結果
# jonny_or_other = session.query(User).where(or_(User.age >=30, User.name == "Jonny Jane")).all()
# print(len(jonny_or_other))
# 與上面的結果相同
# jonny_or_other = session.query(User).where((User.age >=30) | (User.name == "Jonny Jane")).all()
# print(len(jonny_or_other))

# 篩選出不是 jonny 的
# not_jonny = session.query(User).where(not_(User.name == "Jonny Jane")).all()
# print(len(not_jonny))

# 群組化
# users_sexes = session.query(User.sex, func.count(User.sex)).group_by(User.sex).all()
# print(users_sexes)

# 多條件篩選
# users = session.query(User).filter(User.age > 20).filter(User.age < 50).all()
# 下面的寫法等同於上面的
# users = session.query(User).filter(User.age > 20, User.age < 50).all()

# users_tuple = (
#     session.query(User.sex, func.count(User.id))
#     .filter(User.age > 20)
#     .order_by(User.age)
#     .filter(User.age < 50)
#     .group_by(User.sex)
#     .all()
# )
# for sex, count in users_tuple:
#     print(f"Sex: {sex} - {count} users")

# member_1 = Member(name = "John Doe", age = 52)
# member_2 = Member(name = "Eunice Zhou", age = 27)
# member_3 = Member(name = "Joyce Liao", age = 26)

# address_1 = Address(city = "New York", state = "NY", zip_code = "10001")
# address_2 = Address(city = "Los Angeles", state = "CA", zip_code = "90001")
# address_3 = Address(city = "Chicago", state = "Il", zip_code = "60601")
# address_4 = Address(city = "Taipei", state = "TP", zip_code = "23061")

# member_2.addresses.extend([address_1, address_4])
# member_1.addresses.append(address_3)
# member_3.addresses.append(address_2)

# session.add_all([member_3, member_1, member_2])
# session.commit()

merchant1 = Merchant(merchantname = "Zeq Tech 1")
merchant2 = Merchant(merchantname = "Zeq Tech 2")
merchant3 = Merchant(merchantname = "Zeq Tech 3")

merchant1.following.append(merchant2)
merchant2.following.append(merchant3)
merchant3.following.append(merchant1)

session.add_all([merchant1, merchant2, merchant3])
session.commit()

print(f"{merchant1.following = }")
print(f"{merchant2.following = }")
print(f"{merchant3.following = }")