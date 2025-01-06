from fastapi import FastAPI, Depends, Path, HTTPException
import api.models.models as models
from fastapi.middleware.cors import CORSMiddleware
# import api.cruds.get_user as handle_db
import api.cruds.user_info as handle_db
import datetime

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

## 確認用select user list
@app.get(path="/api/users")
async def get_list_user():
    result = handle_db.select_all_user()
    return {
        "status": "OK",
        "data": result
    }
    
## UserRegister
@app.post(path="/register")
async def UserRegister(user_name: str, user_email: str, user_password: str, user_comment: str):
    ## GetCheckEmailDuplication
    result = await handle_db.GetCheckEmailDuplication(user_email)
    if result == 0:
        result = await handle_db.UserRegister(user_name, user_email, user_password, user_comment)
        if result == 1:
            raise HTTPException(status_code=404, detail="Query Error!!")
        return {
            "status": "OK",
            "data": result
        }
    else:
        raise HTTPException(status_code=409, detail="An account with this email already exists.")

## UserLogin
@app.get(path="/login")
async def UserLogin(user_email: str, user_password: str):
    ## GetConfirmConbination
    result = handle_db.GetConfirmConbination(user_email, user_password)
    if result == 1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }

## GetConfirmChangeUserEmail
@app.get(path="/users/{user_id}")
async def GetConfirmChangeUserEmail(user_id: str, user_email: str, new_user_email: str, user_password: str):
    ## GetCheckEmailDuplication
    result = await handle_db.GetConfirmConbination(user_email, user_password) 
    if result == user_id:
        ## GetCheckEmailDuplication
        result = await handle_db.GetCheckEmailDuplication(new_user_email)
        if result == 1:
            raise HTTPException(status_code=404, detail="Query Error!!")
        return {
            "status": "OK",
            "data": result
        }
    else:
        raise HTTPException(status_code=409, detail="No Account.")

## GetPetInfo
@app.get(path="/api/users/info/{user_id}")
async def GetPetInfo(user_id: str):
    result = handle_db.GetPetInfo(user_id)
    if result == 1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }

## ChangeUserEmail
@app.put(path="/users/email/{user_id}")
async def ChangeUserEmail(user_id: str, user_email: str, new_user_email: str, user_password: str):
    ## GetConfirmChangeUserEmail
    user_check = await GetConfirmChangeUserEmail(user_id=user_id, user_email=user_email, new_user_email=new_user_email, user_password=user_password)
    if user_check["status"] == "OK":
        # メールアドレス更新
        result = await handle_db.ChangeUserEmail(user_id, new_user_email)
        if result == 0:
            return {
                "status": "OK",
                "data": result
            }
        else:
            raise HTTPException(status_code=404, detail="Query Error!!")
    raise HTTPException(status_code=409, detail="Unable to change email address")

## ChangeUserPass
@app.put(path="/users/pass/{user_id}")
async def ChangeUserPass(user_id: str, user_email: str, user_password: str, new_user_password: str):
    ## GetConfirmChangeUserEmail
    user_check = await GetConfirmConbination(user_email=user_email, user_password=user_password)
    if user_check["status"] == "OK":
        # メールアドレス更新
        result = await handle_db.ChangeUserPass(user_id, new_user_password)
        if result == 0:
            return {
                "status": "OK",
                "data": result
            }
        else:
            raise HTTPException(status_code=404, detail="Query Error!!")
    raise HTTPException(status_code=409, detail="Unable to change password")

## ChangePetInfo
@app.put(path="/users/info/{user_id}")
async def ChangePetInfo(user_id: str, user_name: str, user_comment: str):
    result = handle_db.ChangePetInfo(user_id, user_name, user_comment)
    if result == 0:
        return {
            "status": "OK",
            "data": result
        }
    else:
        raise HTTPException(status_code=404, detail="Query Error!!")

## DeleteUserAccount
@app.delete(path="/users/{user_id}")
async def DeleteUserAccount(user_id: str, user_email: str, user_password: str):
    ## GetConfirmConbination
    user_check = await handle_db.GetConfirmConbination(user_email=user_email, user_password=user_password)
    if user_check == user_id:
        result = await handle_db.DeleteUserAccount(user_id)
        if result == 1:
            raise HTTPException(status_code=404, detail="Query Error!!")
        return {
            "status": "OK",
            "data": result
        }
    raise HTTPException(status_code=409, detail="no account")
# ## create user
# @app.post(path="/api/users")
# async def post_user(user_name: str, user_mail: str):
#     result = handle_db.create_user(user_name, user_mail)
#     if result == 1:
#         raise HTTPException(status_code=404, detail="Query Error!!")
#     return {
#         "status": "OK",
#         "data": result
#     }

# ## select user
# @app.get(path="/api/users/{user_id}")
# async def get_user(user_id: str):
#     result = handle_db.select_user(user_id)
#     if result == 1:
#         raise HTTPException(status_code=404, detail="Query Error!!")
#     return {
#         "status": "OK",
#         "data": result
#     }

# ## update user 
# @app.put(path="/api/users/{user_id}")
# async def put_user(user_id: str, user_name: str, user_mail: str, user_status: str):
#     result = handle_db.update_user(user_id, user_name, user_mail, user_status)
#     if result == 1:
#         raise HTTPException(status_code=404, detail="Query Error!!")
#     return {
#         "status": "OK",
#         "data": result
#     }

# ## delete user 
# @app.delete(path="/api/users/{user_id}")
# async def delete_user(user_id: str):
#     result = handle_db.delete_user(user_id)
#     if result == 1:
#         raise HTTPException(status_code=404, detail="Query Error!!")
#     return {
#         "status": "OK",
#         "data": result
#     }
