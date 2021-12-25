from typing import Optional
from datetime import date
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_session
from ..models import Operation, Client
from ..schemas.operation import OperationKind, OperationCreate


class OperationsService:
    """Class for working with operations."""

    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get(self, operation_id: int):
        operation = (
            self.session.query(Operation).filter(Operation.id == operation_id).first()
        )
        if not operation:
            raise HTTPException(status.HTTP_404_NOT_FOUND)
        return operation

    def get_many(self, kind: Optional[OperationKind] = None):
        query = self.session.query(Operation)
        if kind:
            query = query.filter_by(kind=kind)
        operations = query.all()
        return operations

    def create(self, operation_data: OperationCreate) -> Operation:
        """Create new operation in database."""
        operation = Operation(**operation_data.dict())
        client = (
            self.session.query(Client)
            .filter(Client.id == operation_data.user_id)
            .first()
        )
        if operation_data.kind == "income":
            client.balance += operation_data.amount
        if operation_data.kind == "outcome":
            if client.balance >= operation_data.amount:
                client.balance -= operation_data.amount
            else:
                raise HTTPException(status_code=400, detail="Not enough funds to pay")
        self.session.add(operation)
        self.session.commit()
        return operation

    def delete(self, operation_id: int):
        """Delete an operation from database."""
        operation = self.get(operation_id)
        self.session.delete(operation)
        self.session.commit()

    def send_money(
        self,
        user_id_from: int,
        user_id_to: int,
        data: date,
        amount: int,
        description: str,
    ):
        """Create two operations for sending money from one client to another."""
        operation_data1 = {
            "user_id": user_id_from,
            "date": data,
            "kind": "outcome",
            "amount": amount,
            "description": description,
        }
        operation_data_create1 = OperationCreate(**operation_data1)
        operation_data2 = {
            "user_id": user_id_to,
            "date": data,
            "kind": "income",
            "amount": amount,
            "description": description,
        }
        operation_data_create2 = OperationCreate(**operation_data2)
        operation1 = self.create(operation_data_create1)
        operation2 = self.create(operation_data_create2)
        return {
            "user_id_from": user_id_from,
            "user_id_to": user_id_to,
            "date": data,
            "amount": amount,
            "description": description,
        }
