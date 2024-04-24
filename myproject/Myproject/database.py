#1、导入sqlashemy部件
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#2、为SQLalchemy定义数据库URL地址
# SQLALCHEMY_DATABASE_URL = "mysql://root:123456@localhost:3306/table_name_base?charset=utf8m64"
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/table_name_base?charset=utf8mb4"


#3、创建sqlalshemy引擎
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#4、创建一个sessionlocal数据库会话
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

#5、创建一个Base类
Base = declarative_base()