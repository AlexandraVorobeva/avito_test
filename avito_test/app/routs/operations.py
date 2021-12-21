from typing import Optional
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from ..schemas.operation import OperationKind, OperationCreate
from ..schemas.operation import Operation as model_Operation
from ..database import get_session
from ..models import Operation
from ..services.operations import OperationsService


router = APIRouter(prefix='/operations', tags=['operations'],)


@router.get('/', response_model=list)
def get_operations(
        kind: Optional[OperationKind] = None,
        services: OperationsService = Depends()
):
    return services.get_many(kind=kind)


@router.get('/{operation_id}', response_model=model_Operation)
def get_operation(
        operation_id: int,
        services: OperationsService = Depends()
):
    return services.get(operation_id)


@router.post('/', response_model=model_Operation)
def create_operation(
        operation_data: OperationCreate,
        service: OperationsService = Depends(),
):
    return service.create(operation_data=operation_data)


@router.delete('/{operation_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_operation(
    operation_id: int,
    service: OperationsService = Depends(),
):
    service.delete(operation_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)