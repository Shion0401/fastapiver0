# ルーティング
from typing import List
import api.schemas.task as task_schema

from fastapi import APIRouter, Depends, HTTPException
router = APIRouter()
from sqlalchemy.ext.asyncio import AsyncSession

import api.cruds.task as task_crud
from api.db import get_db


@router.get("/tasks", response_model=List[task_schema.Task])
async def list_tasks(db: AsyncSession = Depends(get_db)):
    return await task_crud.get_tasks_with_done(db)
