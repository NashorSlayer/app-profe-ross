from fastapi import FastAPI

from routes.user import user
from routes.area import area

app = FastAPI()
app.include_router(user)
app.include_router(area)
