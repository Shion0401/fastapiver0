# テーブルをpythonで処理するために定義する感じ
# 変更したら以下のコマンドで更新
# docker-compose exec demo-app poetry run python -m api.migrate_db


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base


class GetOwnPost(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    title = Column(String(1024))
    caption = Column(String(1024))
    img = Column(String(1024))

# class get_user(Base):
#     __tablename__ = "tasks"

#     id = Column(Integer, primary_key=True)
#     title = Column(String(1024))

#     done = relationship("Done", back_populates="get_user", cascade="delete")


# class Done(Base):
#     __tablename__ = "dones"

#     id = Column(Integer, ForeignKey("tasks.id"), primary_key=True)

#     get_user = relationship("get_user", back_populates="done")