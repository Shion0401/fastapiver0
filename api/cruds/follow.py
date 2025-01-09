# あらゆる操作
# routersのみで呼び出される

import sys
import api.models.models as models
import api.db as databases

sys.dont_write_bytecode = True


## GetConfirmConbination
async def GetConfirmConbination(following, followed):
    session = databases.create_new_session()
    follow = session.query(models.Followlist).\
                filter(models.Followlist.following == following, 
                       models.Followlist.followed == followed).\
                first()           
    if follow == None:
        return "None"
    else:
        return follow.flag
    
## Follow
async def Follow(following, followed):
    session = databases.create_new_session()
    follow = models.Followlist()
    follow.following = following
    follow.followed = followed
    follow.flag = 1
    session.add(follow)
    session.commit()
    return 0

## ChangeFlag
async def ChangeFlag(following, followed, check):
    session = databases.create_new_session()
    follow = session.query(models.Followlist).\
                filter(models.Followlist.following == following, 
                       models.Followlist.followed == followed).\
                first()
    if follow == None:
        return -1 
    elif check == 0:
        follow.flag = 1
    elif check == 1:
        follow.flag = 0
    session.commit()
    return follow.flag


## GetFollow
async def GetFollow(user_id):
    session = databases.create_new_session()
    user = session.query(models.Followlist).\
                filter(models.Followlist.following == user_id).\
                all()           
    if user == None:
        return -1
    else:
        return [follow.followed for follow in user]



