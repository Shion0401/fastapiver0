from fastapi import FastAPI, Depends, Path, HTTPException
import api.models.models as models
from fastapi.middleware.cors import CORSMiddleware
import api.cruds.follow as handle_db
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



## Follow & UnFollow
@app.post(path="/follow")
async def Follow(following: str, followed: str):
    check = await handle_db.GetConfirmConbination(following, followed)
    if check == "None":
        result = await handle_db.Follow(following, followed)
    else:
        result = await handle_db.ChangeFlag(following, followed, check)
    return {
        "status": "OK",
        "data": result
    }

## GetFollow フォローリストをとってくる
@app.get(path="/follow/{user_id}")
async def GetFollow(user_id: str):
    result = await handle_db.GetFollow(user_id)
    if result == -1:
        raise HTTPException(status_code=404, detail="Query Error!!")
    return {
        "status": "OK",
        "data": result
    }
    

##GetFollowInfo = GetPetInfoでいける



    

