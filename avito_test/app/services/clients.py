from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_session
from ..models import Client, Operation
from ..schemas.clients import ClientCreate
from ..services.currency import USD, EUR, CNY


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

    def get_operations_sort_by_days(self, client_id: int, day):
        """Get information about all operations for one user per day."""
        query = self.session.query(Operation)
        operations = query.filter(Operation.user_id == client_id,
                                  Operation.date == day).all()
        return operations

    def get_clients_balance_currency(self, client_id: int, currency: str):
        """Get client's balance from database and convert it from RUB to USD, EUR or CNY"""
        client = self.get(client_id)
        if currency == 'USD':
            client.balance = round(client.balance / USD, 2)
        if currency == 'EUR':
            client.balance = round(client.balance / EUR, 2)
        if currency == 'CNY':
            client.balance = round(client.balance / CNY, 2)
        return client