import uvicorn
from fastapi import FastAPI, APIRouter
from routs import router


app = FastAPI(title="Account", description="by Aexandra Vorobeva")
app.include_router(router)

