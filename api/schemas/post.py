# APIのリクエストやレスポンスの型を定義
# routersとcrudsで用いられる

from typing import Optional
from pydantic import BaseModel, Field

# 初期値
class GetPost_Base(BaseModel):
    title: Optional[str] = Field(None, example="ぽてぽてぽてぽてぽてじん")
    caption: Optional[str] = Field(None, example="uooooo")

# 一覧表示
class GetPost(GetPost_Base):
    id: int

    class Config:
        orm_mode = True

# 作成
# class GetOwnPost_Create(GetOwnPost_Base):
#     pass

# # IDをつけてDBに保存
# class GetOwnPost_Create_Response(GetOwnPost_Create):
#     id: int

#     class Config:
#         orm_mode = True

