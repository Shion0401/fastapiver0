# あらゆる操作
# routersのみで呼び出される

import sys
import api.models.models as models
import api.db as databases

sys.dont_write_bytecode = True


## UserRegister
async def UserRegister(user_name, user_email, user_password, user_comment):
    session = databases.create_new_session()
    user = models.User()
    user.name = user_name
    user.email = user_email
    user.password = user_password
    user.comment = user_comment
    session.add(user)
    session.commit()
    return 0

## GetCheckEmailDuplication
async def GetCheckEmailDuplication(user_email):
    session = databases.create_new_session()
    user = session.query(models.User).\
                filter(models.User.email == user_email).\
                first()           
    if user == None:
        return 0

## UserLogin
## GetConfirmConbination
async def GetConfirmConbination(user_email, user_password):
    session = databases.create_new_session()
    user = session.query(models.User).\
                filter(models.User.email == user_email, 
                       models.User.password == user_password).\
                first()           
    if user == None:
        return 1
    else:
        return user.id


## GetPetInfo
def GetPetInfo(user_id):
    session = databases.create_new_session()
    user = session.query(models.User).\
                filter(models.User.id == user_id).\
                first()           
    if user == None:
        user = ""
    return user.name, user.comment


## 確認用
def select_all_user():
    session = databases.create_new_session()
    user_list = session.query(models.User).\
            all()
    if user_list == None:
        user_list = []
    return user_list



def update_user(user_id, user_name, user_mail):
    session = databases.create_new_session()
    user = session.query(models.User).\
                filter(models.User.id == user_id).\
                first()
    if user == None:
        return 1
    user.name = user_name
    user.email = user_mail
    session.commit()
    return 0

def delete_user(user_id):
    session = databases.create_new_session()
    user = session.query(models.User).\
                filter(models.User.id == user_id).\
                first()
    if user == None:
        return 1
    session.commit()
    return 0






# ChangePetInfo
# ChangeUserPass
# ChangeUserEmail


# DeleteUserAccount