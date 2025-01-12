from fastapi import APIRouter, FastAPI, Depends, Path, HTTPException
import api.models.models as models
from fastapi.middleware.cors import CORSMiddleware
import api.cruds.follow as handle_db
import api.cruds.images as image_db
import datetime

app = FastAPI()
router = APIRouter()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

## Follow & UnFollow
@router.post(path="/follow")
async def Follow(following: str, followed: str):
    check = await handle_db.GetConfirmConbination(following, followed)
    if check == "None":
        result = await handle_db.Follow(following, followed)
    elif check == -1:
        return -1
    else:
        result = await handle_db.ChangeFlag(following, followed, check)
    return result

## GetFollow フォローリストをとってくる
@router.get(path="/follow/{user_id}")
async def GetFollow(user_id: str):
    result = await handle_db.GetFollow(user_id)
    # result = await GetPetInfo(result)
    return result
    
