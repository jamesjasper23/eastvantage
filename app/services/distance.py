from geopy.distance import geodesic
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException

from app.db import models
from app.core.logger import logger


def get_addresses_within_distance(
    db: Session,
    lat: float,
    lon: float,
    distance_km: float
):
    try:
        user_location = (lat, lon)

        addresses = db.query(models.Address).all()

        result = []

        for addr in addresses:
            addr_location = (addr.latitude, addr.longitude)

            dist = geodesic(user_location, addr_location).km

            if dist <= distance_km:
                result.append(addr)

        logger.info(
            f"Retrieved {len(result)} addresses within {distance_km} km"
        )

        return result

    except SQLAlchemyError as e:
        logger.error(f"Database error during distance search: {str(e)}")
        raise HTTPException(status_code=500, detail="Database error")

    except Exception as e:
        logger.error(f"Unexpected error during distance search: {str(e)}")
        raise HTTPException(status_code=500, detail="Unexpected server error")