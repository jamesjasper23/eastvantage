from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.db import models
from app.schemas.address import AddressCreate, AddressUpdate
from app.core.logger import logger
from sqlalchemy.exc import SQLAlchemyError

def create_address(db: Session, address: AddressCreate):
    try:
        db_address = models.Address(**address.model_dump())

        db.add(db_address)
        db.commit()
        db.refresh(db_address)

        logger.info(f"Created address with id={db_address.id}")

        return db_address

    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Database error while creating address: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error")



def update_address(db: Session, address_id: int, data: AddressUpdate):
    try:
        address = db.query(models.Address).filter(
            models.Address.id == address_id
        ).first()

        if not address:
            logger.warning(f"Address {address_id} not found")
            raise HTTPException(status_code=404, detail="Address not found")

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(address, key, value)

        db.commit()
        db.refresh(address)

        logger.info(f"Updated address with id={address_id}")

        return address

    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Database error while updating address: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error")

def delete_address(db: Session, address_id: int):
    try:
        address = db.query(models.Address).filter(
            models.Address.id == address_id
        ).first()

        if not address:
            logger.warning(f"Address {address_id} not found")
            raise HTTPException(status_code=404, detail="Address not found")

        db.delete(address)
        db.commit()

        logger.info(f"Deleted address with id={address_id}")

        return {"message": "Deleted successfully"}

    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Database error while deleting address: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error")

def get_all_addresses(db: Session):
    try:
        addresses = db.query(models.Address).all()

        logger.info(f"Retrieved {len(addresses)} addresses")

        return addresses

    except SQLAlchemyError as e:
        logger.error(f"Database error while retrieving addresses: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error")

    except Exception as e:
        logger.error(f"Unexpected error while retrieving addresses: {str(e)}")
        raise HTTPException(status_code=500, detail="Unexpected server error")