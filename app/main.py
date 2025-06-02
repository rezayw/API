from fastapi import FastAPI
from app.routes import base
from app.core import config

app = FastAPI(title=config.APP_NAME)

app.include_router(base.router, prefix=config.API_PREFIX)
