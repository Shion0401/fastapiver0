# ルーティング
from typing import List
import api.schemas.post as get_post_s
import api.cruds.get_user as get_user_crud

from fastapi import APIRouter, Depends, HTTPException
router = APIRouter()
from sqlalchemy.ext.asyncio import AsyncSession
from api.db import get_db


# GetOwnPost - 自分の投稿を取得
# @router.get("/api/posts/me", response_model=List[get_post_s.GetPost])
# async def list_own_posts(
#     current_user: User = Depends(get_current_user),
#     db: AsyncSession = Depends(get_db)
# ):
#     return await get_user_crud.GetOwnPost(db, current_user.id)

# GetOthersPost - 他のユーザーの投稿を取得
@router.get("/api/users/{user_id}/posts", response_model=List[get_post_s.GetPost])
async def list_user_posts(
    user_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await get_user_crud.GetOthersPost(db, user_id)

# GetNewPost - 新着投稿を取得
# @router.get("/api/posts/recent", response_model=List[get_post_s.GetPost])
# async def list_recent_posts(
#     db: AsyncSession = Depends(get_db)
# ):
#     return await get_user_crud.GetNewPost(db)

# @router.get("/ownpost", response_model=List[get_post_s.GetOwnPost])
# async def list_ownpost(db: AsyncSession = Depends(get_db)):
#     return await get_user_crud.GetOwnPost(db)