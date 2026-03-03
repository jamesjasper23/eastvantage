from fastapi import FastAPI
from app.db.session import engine
from app.db.models import Base
from app.api.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Address Book API")

app.include_router(router)