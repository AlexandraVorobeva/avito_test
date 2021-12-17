from fastapi import APIRouter
from ..database import SessionLocal
from ..models import Operation


router = APIRouter(prefix='/operations')

@router.get('/', response_model=list)
def get_operations():
    session = SessionLocal()
    operations = (session.query(Operation).all())
    return operations