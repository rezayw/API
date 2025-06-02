from fastapi import FastAPI
from app.routes import base, auth  # Tambah auth
from app.core import config
from app.db import models, base as db_base

app = FastAPI(title=config.APP_NAME)

app.include_router(base.router, prefix=config.API_PREFIX)
app.include_router(auth.router, prefix=config.API_PREFIX)

# Buat tabel jika belum ada
db_base.Base.metadata.create_all(bind=db_base.engine)
