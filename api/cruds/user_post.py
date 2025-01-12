import sys
import api.models.models as models
import api.db as databases

import datetime

sys.dont_write_bytecode = True


## Post
def Post(user_id, title, caption):
    session = databases.create_new_session()
    post = models.Post()
    if title is not None:
        post.title = title
    if caption is not None:
        post.caption = caption
    post.create_date_time = datetime.datetime.now()
    post.user_id = user_id  # user_idの設定
    post.goodcount = 0  # 初期値の設定（オプショナル）
    session.add(post)
    session.commit()
    return 0

## GetOnesPost
async def GetOnesPost(user_id):
    session = databases.create_new_session()
    posts = session.query(models.Post).\
                filter(models.Post.user_id == user_id).\
                order_by(models.Post.create_date_time.desc()).\
                limit(10).\
                all()         
    if posts == None:
        posts = -1
    return posts

## GetNewPost
async def GetNewPost():
    session = databases.create_new_session()
    posts = session.query(models.Post).\
                order_by(models.Post.create_date_time.desc()).\
                limit(10).\
                all()     
    if posts == None:
        posts = -1
    return posts

## DeletePost
async def DeletePost(user_id, post_id):
    session = databases.create_new_session()
    post = session.query(models.Post).\
                filter(models.Post.user_id == user_id, models.Post.id == post_id).\
                first()
    if post == None:
        return -1
    session.delete(post)
    session.commit()
    return 0

## GoodCount
async def GoodCount(post_id):
    session = databases.create_new_session()
    post = session.query(models.Post).\
                filter(models.Post.id == post_id).\
                first()         
    if post == None:
        post = -1
    return post.goodcount
    
    
## Good
async def Good(post_id):
    session = databases.create_new_session()
    post = session.query(models.Post).\
                filter(models.Post.id == post_id).\
                first()
    if post == None:
        return -1
    post.goodcount += 1
    session.commit()
    return 0