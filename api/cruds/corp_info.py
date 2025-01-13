# あらゆる操作
# routersのみで呼び出される

import sys
import api.models.models as models
import api.db as databases

sys.dont_write_bytecode = True


## RegisterCorpInfo
async def RegisterCorpInfo(corpname, email, manager):
    session = databases.create_new_session()
    corp_info = models.CorpInfo()
    corp_info.corpname = corpname
    corp_info.email = email
    corp_info.manager = manager
    session.add(corp_info)
    session.commit()
    return corp_info.id

## GetCorpName
# async def GetCorpName(user_email):
#     session = databases.create_new_session()
#     user = session.query(models.User).\
#                 filter(models.User.email == user_email).\
#                 first()           
#     if user == None:
#         return 0

## GetCorpInfo
async def GetCorpInfo(corp_id):
    session = databases.create_new_session()
    corp = session.query(models.CorpInfo).\
                filter(models.CorpInfo.id == corp_id).\
                first()                    
    if corp == None:
        return -1
    else:
        return corp.corpname, corp.email, corp.manager


## DeleteUserAccount
async def DeleteCorpInfo(corp_id):
    session = databases.create_new_session()
    corp = session.query(models.CorpInfo).\
                filter(models.CorpInfo.id == corp_id).\
                first()
    if corp == None:
        return -1
    session.delete(corp)
    session.commit()
    return 0

