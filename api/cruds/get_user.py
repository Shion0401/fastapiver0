# あらゆる操作
# routersのみで呼び出される

import sys
import api.models.models as models
import api.db as databases

sys.dont_write_bytecode = True
def select_all_user():
    session = databases.create_new_session()
    user_list = session.query(models.User).\
            all()
    if user_list == None:
        user_list = []
    return user_list

def create_user(user_name, user_mail):
    session = databases.create_new_session()
    user = models.User()
    user.name = user_name
    user.email = user_mail
    session.add(user)
    session.commit()
    return 0

def select_user(user_id):
    session = databases.create_new_session()
    user = session.query(models.User).\
                filter(models.User.id == user_id).\
                first()           
    if user == None:
        user = ""
    return user

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


