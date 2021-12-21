from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_session
from ..models import Client
from ..schemas.clients import ClientCreate


class ClientService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get(self, client_id: int):
        client_info = (
            self.session
                .query(Client)
                .filter(Client.id == client_id)
                .first()
        )
        if not client_info:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return client_info

    def create(self, client_data: ClientCreate) -> Client:
        operation = Client(**client_data.dict())
        self.session.add(operation)
        self.session.commit()
        return operation

    def delete(self, client_id: int,):
        client = self.get(client_id)
        self.session.delete(client)
        self.session.commit()
