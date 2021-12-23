from typing import Optional, List
from datetime import date
from fastapi import APIRouter, Depends, Response, status
from ..schemas.operation import OperationKind, OperationCreate
from ..schemas.operation import Operation as model_Operation
from ..services.operations import OperationsService


router = APIRouter(prefix='/operations', tags=['operations'],)


@router.get('/', response_model=List[model_Operation])
def get_operations(
        kind: Optional[OperationKind] = None,
        services: OperationsService = Depends()
):
    """GET information about all operations in database."""
    return services.get_many(kind=kind)


@router.get('/{operation_id}', response_model=model_Operation)
def get_operation(
        operation_id: int,
        services: OperationsService = Depends()
):
    """GET information about an operation by id."""
    return services.get(operation_id)


@router.post('/', response_model=model_Operation)
def create_operation(
        operation_data: OperationCreate,
        service: OperationsService = Depends(),
):
    """POST (create) new operation. Operation can be 'income' or 'outcome' kind."""
    return service.create(operation_data=operation_data)


@router.delete('/{operation_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_operation(
    operation_id: int,
    service: OperationsService = Depends(),
):
    """DELETE any operation by id."""
    service.delete(operation_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.post('/send_money/{user_id_from}/{user_id_to}')
def send_money_from_client_to_client(
        user_id_from: int,
        user_id_to: int,
        data: date,
        amount: int,
        description: str,
        service: OperationsService = Depends(),
):
    """Sent money from one client to another."""
    return service.send_money(user_id_from, user_id_to, data, amount, description)