# ルーティング
from typing import List
import api.schemas.get_user as get_user_schema
import api.cruds.get_user as get_user_crud

from fastapi import APIRouter, Depends, HTTPException
router = APIRouter()
from sqlalchemy.ext.asyncio import AsyncSession
from api.db import get_db


# GetOwnPost
@router.get("/ownpost", response_model=List[get_user_schema.GetOwnPost])
async def list_tasks(db: AsyncSession = Depends(get_db)):
    return await get_user_crud.GetOwnPost(db)
