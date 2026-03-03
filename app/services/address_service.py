from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.db import models
from app.schemas.address import AddressCreate, AddressUpdate
from app.core.logger import logger


def create_address(db: Session, address: AddressCreate):
    db_address = models.Address(**address.model_dump())

    db.add(db_address)
    db.commit()
    db.refresh(db_address)

    logger.info(f"Created address with id={db_address.id}")

    return db_address


def update_address(db: Session, address_id: int, data: AddressUpdate):
    address = db.query(models.Address).filter(models.Address.id == address_id).first()

    if not address:
        logger.warning(f"Address {address_id} not found for update")
        raise HTTPException(status_code=404, detail="Address not found")

    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(address, key, value)

    db.commit()
    db.refresh(address)

    logger.info(f"Updated address with id={address_id}")

    return address


def delete_address(db: Session, address_id: int):
    address = db.query(models.Address).filter(models.Address.id == address_id).first()

    if not address:
        logger.warning(f"Address {address_id} not found for delete")
        raise HTTPException(status_code=404, detail="Address not found")

    db.delete(address)
    db.commit()

    logger.info(f"Deleted address with id={address_id}")

    return {"message": "Deleted successfully"}