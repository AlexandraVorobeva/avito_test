from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_session
from ..models import Operation
from ..schemas.operation import OperationKind, OperationCreate


class OperationsService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_many(self, kind: Optional[OperationKind] = None):
        query = self.session.query(Operation)
        if kind:
            query = query.filter_by(kind=kind)
        operations = query.all()
        return operations


    def create(self, operation_data: OperationCreate) -> Operation:
        operation = Operation(**operation_data.dict())
        self.session.add(operation)
        self.session.commit()
        return operation