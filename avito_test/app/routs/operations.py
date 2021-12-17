from fastapi import APIRouter
# from database import SessionLocal


router = APIRouter(prefix='/operations')

@router.get('/', response_model=list)
def get_operations():
    pass
    # session = SessionLocal()
    # operations = (session.query(Operation).all())
    # return operations