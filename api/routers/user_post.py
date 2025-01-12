from fastapi import APIRouter, FastAPI, Depends, Path, HTTPException, Query
import api.models.models as models
from fastapi.middleware.cors import CORSMiddleware
import api.cruds.images as image_db
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


## Post
@router.post(path="/post")
async def Post(user_id: str, image: str, title: str = Query(None), caption: str = Query(None)):
    postid = handle_db.Post(user_id, title, caption)
    return postid
    # if postid == -1:
    #     return -1
    # InsertPostImageを呼び出す
    # result = image_db.InsertPostImage(postid, image)
    # return result

## GetOnesPost
@router.get(path="/post/get/{user_id}")
async def GetOnesPost(user_id: str):
    result = await handle_db.GetOnesPost(user_id)
    if result == -1:
        return -1
    posts = [
        {
            "title": post.title,
            "caption": post.caption,
            "goodcount": post.goodcount,
            "postimage": post.image
        }
        for post in result
    ]
    return {"posts": posts}
    # GetPostImageを呼び出す
    # if result == -1:
    #     return -1
    # posts = [
    #     {
    #         "title": post.title,
    #         "caption": post.caption,
    #         "goodcount": post.goodcount,
    #         "image": image_db.GetPostImage(post.image)
    #     }
    #     for post in result
    # ]
    # return {"posts": posts}
 
## GetNewPost
@router.get(path="/post/new")
async def GetNewPost():
    result = await handle_db.GetNewPost()
    if result == -1:
        return -1
    posts = [
        {
            "title": post.title,
            "caption": post.caption,
            "goodcount": post.goodcount,
            "postid": post.image
        }
        for post in result
    ]
    return {"posts": posts}
    # GetPostImageを呼び出す
    # if result == -1:
    #     return -1
    # posts = [
    #     {
    #         "title": post.title,
    #         "caption": post.caption,
    #         "goodcount": post.goodcount,
    #         "image": image_db.GetPostImage(post.image)
    #     }
    #     for post in result
    # ]
    # return {"posts": posts}
 

## DeletePost 
@router.delete(path="/post/delete/{user_id}/{post_id}")
async def DeletePost(user_id: str, post_id: str):
    # DeletePostImageを呼び出す
    # result = await image_db.DeletePostImage(user_id, post_id)
    # if result == -1:
    #     return -1
    result = await handle_db.DeletePost(user_id, post_id)
    return result

# GoodCount
@router.get(path="/post/goodcount/{post_id}")
async def GoodCount(post_id: str):
    result = await handle_db.GoodCount(post_id)
    return result

## Good
@router.put(path="/post/good/{post_id}")
async def Good(post_id: str):
    result = await handle_db.Good(post_id)
    return result
