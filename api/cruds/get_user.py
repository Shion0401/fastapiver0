# あらゆる操作

from sqlalchemy.ext.asyncio import AsyncSession

import api.models.get_user as get_user_model
import api.schemas.get_user as get_user_schema
from typing import List, Tuple, Optional

from sqlalchemy import select
from sqlalchemy.engine import Result


async def GetOwnPost(
    db: AsyncSession, get_own_post: get_user_schema.GetOwnPost
) -> get_user_model.GetOwnPost:
    test = get_user_model.GetOwnPost(**get_own_post.dict())
    db.add(test)
    await db.commit()
    await db.refresh(test)
    return test

# async def get_get_user(db: AsyncSession, get_user_id: int) -> Optional[get_user_model.get_user]:
#     result: Result = await db.execute(
#         select(get_user_model.get_user).filter(get_user_model.get_user.id == get_user_id)
#     )
#     get_user: Optional[Tuple[get_user_model.get_user]] = result.first()
#     return get_user[0] if get_user is not None else None  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す

# async def get_get_users_with_done(db: AsyncSession) -> List[Tuple[int, str, bool]]:
#     result: Result = await (
#         db.execute(
#             select(
#                 get_user_model.get_user.id,
#                 get_user_model.get_user.title,
#                 get_user_model.Done.id.isnot(None).label("done"),
#             ).outerjoin(get_user_model.Done)
#         )
#     )
#     return result.all()


# async def update_get_user(
#     db: AsyncSession, get_user_create: get_user_schema.get_userCreate, original: get_user_model.get_user
# ) -> get_user_model.get_user:
#     original.title = get_user_create.title
#     db.add(original)
#     await db.commit()
#     await db.refresh(original)
#     return original

# async def delete_get_user(db: AsyncSession, original: get_user_model.get_user) -> None:
#     await db.delete(original)
#     await db.commit()