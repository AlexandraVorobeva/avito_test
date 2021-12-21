from typing import Optional
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from ..schemas.clients import ClientCreate
from ..schemas.clients import Client as model_Client
from ..database import get_session
from ..models import Client
from ..services.clients import ClientService


router = APIRouter(prefix='/clients', tags=['clients'],)


@router.get('/{client_id}', response_model=model_Client)
def get_client(
        client_id: int,
        services: ClientService = Depends()
):
    return services.get(client_id)


@router.post('/', response_model=model_Client)
def create_client(
        client_data: ClientCreate,
        service: ClientService = Depends(),
):
    return service.create(client_data=client_data)


@router.delete('/{client_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_operation(
    client_id: int,
    service: ClientService = Depends(),
):
    service.delete(client_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)