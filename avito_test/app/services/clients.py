from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_session
from ..models import Client, Operation
from ..schemas.clients import ClientCreate


class ClientService:
    """Class for working with clients."""
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get(self, client_id: int):
        """Get information about any client in  database by id."""
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
        """Create new client in database."""
        operation = Client(**client_data.dict())
        self.session.add(operation)
        self.session.commit()
        return operation

    def delete(self, client_id: int,):
        """Delete any client from database."""
        client = self.get(client_id)
        self.session.delete(client)
        self.session.commit()

    def get_operations_for_user(self, client_id: int):
        """Get information about all operations for one user by user id from database."""
        query = self.session.query(Operation)
        if client_id:
            query = query.filter(Operation.user_id == client_id)
        operations = query.all()
        return operations

