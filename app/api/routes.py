from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.address import AddressCreate, AddressUpdate, AddressResponse
from app.services.address_service import (
    create_address,
    update_address,
    delete_address,
)

router = APIRouter(prefix="/addresses", tags=["Addresses"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=AddressResponse)
def create(address: AddressCreate, db: Session = Depends(get_db)):
    return create_address(db, address)


@router.put("/{address_id}", response_model=AddressResponse)
def update(address_id: int, data: AddressUpdate, db: Session = Depends(get_db)):
    return update_address(db, address_id, data)


@router.delete("/{address_id}")
def delete(address_id: int, db: Session = Depends(get_db)):
    return delete_address(db, address_id)