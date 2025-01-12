from fastapi import APIRouter, FastAPI, Depends, Path, HTTPException
import api.models.models as models
from fastapi.middleware.cors import CORSMiddleware
import api.cruds.report as handle_db
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

## GetReport
@router.get(path="/report/report/count/{user_id}")
async def GetReport(user_id: str):
    result = await handle_db.GetReport(user_id)
    return {
        "status": "OK",
        "data": result
    }
    

## Insert&UpdateReport
@router.put(path="/report/report/count/{user_id}")
async def InsertUpdateReport(user_id: str):
    result = await handle_db.GetReport(user_id)
    if result == 'None':
        result = await handle_db.InsertReport(user_id)
    else:
        result = await handle_db.UpdateReport(user_id)
        if result == -1:
            raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }


## ExclusionViolationUser
@router.delete(path="/report/post/exclusive/{user_id}")
async def ExclusionViolationUser(user_id: str):
    result = handle_db.DeleteReport(user_id)
    if result == -1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }
    


