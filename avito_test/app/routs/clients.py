from typing import Optional, List
from fastapi import APIRouter, Depends, Response, status
from ..schemas.clients import ClientCreate
from ..schemas.clients import Client as model_Client
from ..schemas.currency import CurrencyKind
from ..schemas.operation import Operation as model_Operation
from ..services.clients import ClientService


router = APIRouter(prefix='/clients', tags=['clients'],)


@router.get('/{client_id}', response_model=model_Client)
def get_all_info_about_client(
        client_id: int,
        services: ClientService = Depends()
):
    """GET information about a client by id."""
    return services.get(client_id)



@router.post('/', response_model=model_Client)
def create_client(
        client_data: ClientCreate,
        service: ClientService = Depends(),
):
    """POST (create) new client."""
    return service.create(client_data=client_data)


@router.delete('/{client_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_client(
    client_id: int,
    service: ClientService = Depends(),
):
    """DELETE any client by id."""
    service.delete(client_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.get('/all_operations/{client_id}')
def get_operations_for_client(
        client_id: int,
        services: ClientService = Depends()
):
    """GET information about all operations for one user by user id."""
    return services.get_operations_for_user(client_id)


@router.get('/operations_per_day/{client_id}/{day}', response_model=List[model_Operation])
def get_operations_per_day(
        client_id: int,
        day,
        services: ClientService = Depends()
):
    """GET information about all operations for one user per day."""
    return services.get_operations_sort_by_days(client_id, day)


@router.get('/{client_id}/{currency}', response_model=model_Client)
def get_clients_balance(
        client_id: int,
        currency: CurrencyKind,
        services: ClientService = Depends()
):
    """GET client's balance in different currencies."""
    return services.get_clients_balance_currency(client_id, currency)