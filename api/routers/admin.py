# swaggerでデバッグしてませんごめんなさい
# 通報されてないんですx

from fastapi import APIRouter, FastAPI, Depends, Path, HTTPException
import api.models.models as models
from fastapi.middleware.cors import CORSMiddleware
import api.cruds.admin as handle_db
import api.cruds.images as image_db
import datetime

app = FastAPI()
router = APIRouter()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

## AdminRegister
@router.post(path="/admin/account/register")
async def AdminRegister(admin_name: str, admin_email: str, admin_password: str):
    ## GetCheckEmailDuplication
    result = await handle_db.GetCheckEmailDuplication(admin_email)
    if result == 0:
        result = await handle_db.AdminRegister(admin_name, admin_email, admin_password)
        return result

## AdminLogin
@router.get(path="/admin/login")
async def AdminLogin(admin_email: str, admin_password: str):
    ## GetConfirmConbination
    result = await handle_db.GetConfirmConbination(admin_email, admin_password)
    return result

## GetViolationUser
@router.get(path="/admin/ViolationUser")
async def GetViolationUser():
    result = await handle_db.GetViolationUser()
    return result    
    
## GetViolationUserInfo
@router.get(path="/admin/ViolationUser/{user_id}")
async def GetViolationUserInfo(user_id: str):
    result = await handle_db.GetViolationUserInfo(user_id)
    return result    

## DeleteViolationUser
@router.delete(path="/admin/delete/{user_id}")
async def DeleteViolationUser(user_id: str):
    result = await handle_db.DeleteViolationUser(user_id)
    return result