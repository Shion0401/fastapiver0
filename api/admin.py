# swaggerでデバッグしてませんごめんなさい
# 通報されてないんですx

from fastapi import FastAPI, Depends, Path, HTTPException
import api.models.models as models
from fastapi.middleware.cors import CORSMiddleware
import api.cruds.admin as handle_db
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
# GetAdImage


## AdminLogin
@app.get(path="/login")
async def AdminLogin(admin_email: str, admin_password: str):
    ## GetConfirmConbination
    result = handle_db.GetConfirmConbination(admin_email, admin_password)
    if result == -1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }


## GetViolationUser
@app.get(path="/ViolationUser")
async def GetViolationUser():
    result = await handle_db.GetViolationUser()
    if result == 1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }
    
    
## GetViolationUserInfo
@app.get(path="/ViolationUser/{user_id}")
async def GetViolationUserInfo(user_id: str):
    result = await handle_db.GetViolationUserInfo(user_id)
    if result == -1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }
    

## DeleteViolationUser
@app.delete(path="/delete/{user_id}")
async def DeleteViolationUser(user_id: str):
    result = await handle_db.DeleteViolationUser(user_id)
    if result == -1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }