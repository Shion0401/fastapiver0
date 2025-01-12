# あらゆる操作
# routersのみで呼び出される

import sys
import api.models.models as models
import api.db as databases

sys.dont_write_bytecode = True


## GetConfirmConbination
async def GetConfirmConbination(following, followed):
    session = databases.create_new_session()
    user_exists = session.query(models.User).\
                    filter(models.User.id == following).\
                    first()
    follow_exists = session.query(models.User).\
                    filter(models.User.id == followed).\
                    first()
    if not user_exists or not follow_exists:
        return -1
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

## ChangeFlag（0:フォロー解除中, 1:フォロー中）
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
    return 0


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


#参考## GetPetInfo
# @router.get(path="/user_info/info/{user_id}")
# async def GetPetInfo(user_id: str):
#     result = handle_db.GetPetInfo(user_id)
#     ###########
#     if result == -1:
#         return -1
#     else:
#         return {
#             "name": result[0],
#             "comment": result[1],
#     }
    ###########
    # 成功していればGetIconを呼び出す
    # if result == -1:
    #     return -1
    # else:
    #     data = result
    #     icon = image_db.GetIcon(user_id)
    #     if icon == -1:
    #         return -1
    #     else:
    #         return {
    #             "name": data[0],
    #             "comment": data[1],
    #             "icon": icon
    #         }
