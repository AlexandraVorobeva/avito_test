from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.operation import OperationKind, OperationCreate
from ..schemas.operation import Operation as model_Operation
from ..database import get_session
from ..models import Operation
from ..services.operations import OperationsService


router = APIRouter(prefix='/operations')


@router.get('/', response_model=list)
def get_operations(
        kind: Optional[OperationKind] = None,
        services: OperationsService = Depends()
):
    return services.get_many(kind=kind)


@router.post('/', response_model=model_Operation)
def create_operations(
        operation_data: OperationCreate,
        service: OperationsService = Depends(),
):
    return service.create(operation_data=operation_data)
