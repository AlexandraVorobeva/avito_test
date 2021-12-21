from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_session
from ..models import Operation, Client
from ..schemas.operation import OperationKind, OperationCreate


class OperationsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get(self, operation_id: int):
        operation = (
            self.session
                .query(Operation)
                .filter(Operation.id == operation_id)
                .first()
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
        operation = Operation(**operation_data.dict())
        client = (
            self.session.query(Client)
            .filter(Client.id == operation_data.user_id)
            .first()
        )
        client.balance += operation_data.amount
        self.session.add(operation)
        self.session.commit()
        return operation

    def delete(self, operation_id: int,):
        operation = self.get(operation_id)
        self.session.delete(operation)
        self.session.commit()