from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, JSON
from sqlalchemy.orm import relationship
# 1.用Base类创建SQLALchemy模型
from .database import Base

# class User(Base):
#     __tablename__ = "users"
#     #2.创建模型属性/列
#     id = Column(Integer, primary_key=True, index=True)
#     phone = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)
#     #3.创建关系
#     items = relationship("Item", back_populates="owner")

# # Column 表示这些属性中的每一个都代表其相应数据库表中的一列
# # Column 中的第一个参数，如Integer、String 和 Boolean，它定义了数据库中的类型。
# # primary_key=True 代表了 id 为主键；
# # index=True 代表 id 列和 email 列为索引，以提高查询性能；
# # unique=True 则是唯一约束，以确保在 email 列中的每个值都是唯一的；
# # default=True 表示is_active 的默认值为 True。


# class Item(Base):
#     __tablename__ = "items"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id")) 
#     owner = relationship("User", back_populates="items")


class BasicSetting(Base):
    __tablename__ = "basicsetting"
    id = Column(Integer, primary_key=True, index=True)
    setting_type = Column(String(50))
    setting_content = Column(JSON)

