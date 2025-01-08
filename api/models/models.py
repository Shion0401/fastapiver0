# テーブルをpythonで処理するために定義する感じ
# 変更したら以下のコマンドで更新
# crudsのみで呼び出される

import datetime
import uuid
import sys
from sqlalchemy import (Column, String, Text, ForeignKey,CHAR, VARCHAR, INT,  \
                create_engine, MetaData, DECIMAL, DATETIME, exc, event, Index, \
                and_)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

sys.dont_write_bytecode = True

base = declarative_base()

class User(base):
    __tablename__ = 'user'
    id = Column(CHAR(36), primary_key=True)
    name = Column(VARCHAR(10))
    email = Column(VARCHAR(30))
    password = Column(VARCHAR(64))
    comment = Column(VARCHAR(100))
    # status = Column(VARCHAR(255))
    # image = Column(VARCHAR(255))
    post = relationship("Post", back_populates="user")

    def __init__(self):
        self.id = str(uuid.uuid4())
        
        
class Post(base):
    __tablename__ = 'post'
    id = Column(CHAR(36), primary_key=True)
    title = Column(VARCHAR(17))
    caption = Column(VARCHAR(50))
    create_date_time = Column(DATETIME)
    goodcount = Column(INT, default=0)
    user_id = Column(CHAR(36), ForeignKey("user.id"))  # 型を一致させる
    user = relationship("User", back_populates="post")

    def __init__(self):
        self.id = str(uuid.uuid4())
        now_data_time = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
        self.create_date_time = now_data_time
       
        
# class Followlist(base):
#     __tablename__ = 'followlist'    
#     following = Column(INT, ForeignKey("user.id"))
#     followed = Column(INT, ForeignKey("user.id"))
#     user = relationship("User", back_populates="followlist")

#     def __init__(self):
#         self.id = str(uuid.uuid4())
        
        
# class Report(base):
#     __tablename__ = 'report'    
#     id = Column(CHAR(36), primary_key=True)
#     times = Column(INT(10))
#     update_date_time = Column(DATETIME)
#     user_id = Column(INT, ForeignKey("user.id"))
#     user = relationship("User", back_populates="post")

#     def __init__(self):
#         self.id = str(uuid.uuid4())
#         now_data_time = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))
#         self.update_date_time = now_data_time
        


# class Admin(base):
#     __tablename__ = 'admin'
#     id = Column(CHAR(36), primary_key=True)
#     name = Column(VARCHAR(10))
#     email = Column(VARCHAR(30))
#     password = Column(VARCHAR(64))

#     def __init__(self):
#         self.id = str(uuid.uuid4())
        
        
# class CorpInfo(base):
#     __tablename__ = 'corpinfo'
#     id = Column(CHAR(36), primary_key=True)
#     name = Column(VARCHAR(30))
#     email = Column(VARCHAR(30))
#     manager = Column(VARCHAR(30))
#     # url = Column(VARCHAR(128))
#     # image = Column(VARCHAR(255))

#     def __init__(self):
#         self.id = str(uuid.uuid4())