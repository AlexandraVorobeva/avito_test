from fastapi import APIRouter
from .operations import router as operations_router
from .clients import router as clients_router


router = APIRouter()
router.include_router(clients_router)
router.include_router(operations_router)
