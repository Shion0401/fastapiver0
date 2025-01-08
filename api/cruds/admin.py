# あらゆる操作
# routersのみで呼び出される

import sys
import api.models.models as models
import api.db as databases

sys.dont_write_bytecode = True


## GetConfirmConbination
async def GetConfirmConbination(admin_email, admin_password):
    session = databases.create_new_session()
    admin = session.query(models.Admin).\
                filter(models.Admin.email == admin_email, 
                       models.Admin.password == admin_password).\
                first()           
    if admin == None:
        return 1
    else:
        return admin.id

## GetCorpName
# async def GetCorpName(Admin_email):
#     session = databases.create_new_session()
#     Admin = session.query(models.Admin).\
#                 filter(models.Admin.email == Admin_email).\
#                 first()           
#     if Admin == None:
#         return 0

## GetViolationUser
async def GetViolationUser():
    session = databases.create_new_session()
    report = session.query(models.Report).\
                filter(models.Report.times > 1).\
                all()                    
    if report == None:
        return -1
    else:
        return report.user_id, report.times


## GetViolationUserInfo
async def GetViolationUserInfo(user_id):
    session = databases.create_new_session()
    user = session.query(models.User).\
                filter(models.User.id == user_id).\
                first()                    
    if user == None:
        return -1
    else:
        return user


## DeleteViolationUser
async def DeleteViolationUser(cuser_id):
    session = databases.create_new_session()
    user = session.query(models.User).\
                filter(models.User.id == user_id).\
                first()
    if user == None:
        return -1
    session.delete(user)
    session.commit()
    return 0

