from typing import List, Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi import status
from src.codeplaceholder.models.operation import Operation, OperationKind, OperationCreate, OperationUpdate
from src.codeplaceholder.services.operation import OperationService

router = APIRouter(
    prefix='/operations'
)


@router.get('/', response_model=List[Operation])
def get_operations(
        kind: Optional[OperationKind] = None,
        gt_price: Optional[int] = None,
        lt_price: Optional[int] = None,
        service: OperationService = Depends()
):
    return service.get_list(kind=kind, gt_price=gt_price, lt_price=lt_price)


@router.get('/{id}', response_model=Operation)
def get_operation_by_id(operation_id: int, service: OperationService = Depends()):
    return service.get_by_id(operation_id)


@router.post('/', response_model=Operation)
def create_operations(
        operation_data: OperationCreate,
        service: OperationService = Depends()
):
    return service.create(operation_data)


@router.put('/{id}', response_model=Operation)
def update_operation(
        operation_id: int,
        operation_data: OperationUpdate,
        service: OperationService = Depends()
):
    return service.update(operation_id, operation_data)


@router.delete('/{id}')
def delete_operation(operation_id: int, service: OperationService = Depends()):
    service.delete(operation_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
