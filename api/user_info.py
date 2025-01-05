from fastapi import FastAPI, Depends, Path, HTTPException
import api.models.models as models
from fastapi.middleware.cors import CORSMiddleware
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

# 一旦放置
# InsertIcon
# GetIcon
# ChangeIcon
# DeleteIcon

## UserRegister
@app.post(path="/register")
async def post_user(user_name: str, user_email: str, user_password: str, user_comment: str):
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
## GetConfirmConbination
@app.get(path="/login")
async def get_user(user_email: str, user_password: str):
    result = handle_db.GetConfirmConbination(user_email, user_password)
    if result == 1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }


## GetConfirmChangeUserEmail
@app.get(path="/users/email/{user_id}")
async def get_user(user_id: str, user_email: str, new_user_email: str, user_password: str):
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
async def get_user(user_id: str):
    result = handle_db.GetPetInfo(user_id)
    if result == 1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }


## 確認用select user list
@app.get(path="/api/users")
async def get_list_user():
    result = handle_db.select_all_user()
    return {
        "status": "OK",
        "data": result
    }




## update user 
@app.put(path="/api/users/{user_id}")
async def put_user(user_id: str, user_name: str, user_mail: str, user_status: str):
    result = handle_db.update_user(user_id, user_name, user_mail, user_status)
    if result == 1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }

## delete user 
@app.delete(path="/api/users/{user_id}")
async def delete_user(user_id: str):
    result = handle_db.delete_user(user_id)
    if result == 1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }












# ChangePetInfo
# ChangeUserPass
# ChangeUserEmail


# DeleteUserAccount