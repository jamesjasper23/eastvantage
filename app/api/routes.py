from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.address import AddressCreate, AddressUpdate, AddressResponse
from app.services.address_service import (
    create_address,
    update_address,
    delete_address,
)
from app.services.distance import get_addresses_within_distance
from app.services.address_service import get_all_addresses

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

@router.get("/near", response_model=list[AddressResponse])
def get_nearby_addresses(
    lat: float,
    lon: float,
    distance: float,
    db: Session = Depends(get_db)
):
    return get_addresses_within_distance(db, lat, lon, distance)

@router.get("/", response_model=list[AddressResponse])
def get_addresses(db: Session = Depends(get_db)):
    return get_all_addresses(db)