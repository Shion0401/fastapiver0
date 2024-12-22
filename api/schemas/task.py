# APIのリクエストやレスポンスの型を定義

from typing import Optional
from pydantic import BaseModel, Field


class TaskBase(BaseModel):
    title: Optional[str] = Field(None, example="クリーニングを取りに行く")

# 作成
class TaskCreate(TaskBase):
    pass

# IDをつけて返す
class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True

# 一覧表示
class Task(TaskBase):
    id: int
    done: bool = Field(False, description="完了フラグ")

    class Config:
        orm_mode = True