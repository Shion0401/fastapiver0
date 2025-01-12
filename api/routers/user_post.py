from fastapi import APIRouter, FastAPI, Depends, Path, HTTPException
import api.models.models as models
from fastapi.middleware.cors import CORSMiddleware
# import api.cruds.get_user as handle_db
import api.cruds.user_post as handle_db
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

# 一旦放置
# DeletePostImage
# InsertPostImage
# GetPostImage

## Post
@router.post(path="/post")
async def Post(user_id: str, title: str, caption: str):
    result = handle_db.Post(user_id, title, caption)
    if result == 0:
        return {
            "status": "OK",
            "data": result
        }
    raise HTTPException(status_code=404, detail="Query Error!!")
   

## GetOnesPost
@router.get(path="/post/get/{user_id}")
async def GetOnesPost(user_id: str):
    result = handle_db.GetOnesPost(user_id)
    if result == 1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }

    
## GetNewPost p13
@router.get(path="/post/new")
async def GetNewPost():
    result = handle_db.GetNewPost()
    if not result:  # 空のリストやNoneの場合
        raise HTTPException(status_code=404, detail="No posts found.")
    return {
        "status": "OK",
        "data": result
    }


## DeletePost 
@router.delete(path="/post/{user_id}/{post_id}")
async def DeletePost(user_id: str, post_id: str):
    result = handle_db.DeletePost(user_id, post_id)
    if result == 1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }
    

# GoodCount
@router.get(path="/post/goodcount/{post_id}")
async def GoodCount(post_id: str):
    print("post")
    result = await handle_db.GoodCount(post_id)
    if result == -1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }  
    

## Good
@router.put(path="/post/good/{post_id}")
async def Good(post_id: str):
    result = await handle_db.GoodCount(post_id)
    if result == -1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    result = await handle_db.Good(post_id)
    if result == -1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }
