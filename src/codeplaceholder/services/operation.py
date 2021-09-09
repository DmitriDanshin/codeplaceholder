from typing import List, Optional

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from codeplaceholder import tables
from codeplaceholder.database import get_session
from codeplaceholder.models.operation import OperationKind, OperationCreate, OperationUpdate


class OperationService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def _get(self, operation_id: int) -> tables.Operation:
        operation = self.session.get(tables.Operation, operation_id)
        if not operation:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return operation

    def get_list(self,
                 kind: Optional[OperationKind] = None,
                 gt_price: Optional[int] = None,
                 lt_price: Optional[int] = None) -> List[tables.Operation]:
        db = tables.Operation
        query = self.session.query(db)
        if kind:
            query = query.filter_by(kind=kind)
        if gt_price:
            query = query.filter(db.amount >= gt_price)
        if lt_price:
            query = query.filter(db.amount <= lt_price)

        operations = query.all()
        return operations

    def get_by_id(self, operation_id: int) -> tables.Operation:
        return self._get(operation_id)

    def create(self, operation_data: OperationCreate) -> tables.Operation:
        operation = tables.Operation(**operation_data.dict())
        self.session.add(operation)
        self.session.commit()
        return operation

    def update(self, operation_id: int, operation_data: OperationUpdate) -> tables.Operation:
        operation = self._get(operation_id)
        for field, value in operation_data:
            setattr(operation, field, value)
        self.session.commit()
        return operation

    def delete(self, operation_id: int):
        operation = self._get(operation_id)
        self.session.delete(operation)
        self.session.commit()
