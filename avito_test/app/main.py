import uvicorn
from fastapi import FastAPI, APIRouter
from .routs import router
from .database import engine, Base

Base.metadata.create_all(engine)

app = FastAPI(
    title="Account", description="Avito intern assignment by Aexandra Vorobeva"
)
app.include_router(router)
