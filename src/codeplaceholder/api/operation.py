from typing import List

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from codeplaceholder import tables
from src.codeplaceholder.database import get_session
from src.codeplaceholder.models.operation import Operation

router = APIRouter(
    prefix='/operations'
)


@router.get('/', response_model=List[Operation])
def get_operations(session: Session = Depends(get_session)):
    operations = session.query(tables.Operation).all()
    return operations

