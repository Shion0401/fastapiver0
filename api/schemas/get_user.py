# APIのリクエストやレスポンスの型を定義

from typing import Optional
from pydantic import BaseModel, Field

# 初期値
class GetOwnPost_Base(BaseModel):
    title: Optional[str] = Field(None, example="ぽてぽてぽてぽてぽてじん")

# 作成
class GetOwnPost_Create(GetOwnPost_Base):
    pass

# IDをつけてDBに保存
class GetOwnPost_Create_Response(GetOwnPost_Create):
    id: int

    class Config:
        orm_mode = True

# 一覧表示
class GetOwnPost(GetOwnPost_Base):
    id: int

    class Config:
        orm_mode = True