from fastapi import FastAPI

from api.routers import task, done, get_user, get_admin

app = FastAPI()
# app.include_router(task.router)
# app.include_router(done.router)
app.include_router(get_user.router)