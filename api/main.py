from fastapi import FastAPI

from api.routers import user_info, user_post, report, admin, corp_info, follow

app = FastAPI()
app.include_router(user_info.router)
app.include_router(user_post.router)
app.include_router(report.router)
app.include_router(admin.router)
app.include_router(corp_info.router)
app.include_router(follow.router)