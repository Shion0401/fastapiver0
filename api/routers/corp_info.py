from fastapi import APIRouter, FastAPI, Depends, Path, HTTPException
import api.models.models as models
from fastapi.middleware.cors import CORSMiddleware
import api.cruds.corp_info as handle_db
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

# 一旦放置
# ChangeAdImage
# DeleteAdImage
# InsertAdImage


## RegisterCorpInfo
@router.post(path="/corp_info/register")
async def RegisterCorpInfo(corpname: str, email: str, manager: str):
    result = await handle_db.RegisterCorpInfo(corpname, email, manager)
    if result == -1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }


## GetCorpName
# @router.get(path="/corp_info/corpname")
# async def GetCorpName(user_email: str, user_password: str):
#     result = handle_db.GetConfirmConbination(user_email, user_password)
#     if result == 1:
#         raise HTTPException(status_code=404, detail="Query Error!!")
#     return {
#         "status": "OK",
#         "data": result
#     }
    
    
## GetCorpInfo
@router.get(path="/corp_info/corpinfo/{corp_id}")
async def GetCorpInfo(corp_id: str):
    result = await handle_db.GetCorpInfo(corp_id)
    if result == -1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }
    

## DeleteCorpInfo
@router.delete(path="/corp_info/corp/delete/{corp_id}")
async def DeleteCorpInfo(corp_id: str):
    result = await handle_db.DeleteCorpInfo(corp_id)
    if result == -1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }