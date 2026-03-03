from pydantic import BaseModel, Field
from typing import Optional

class AddressCreate(BaseModel):
    name: str = Field(..., min_length=1)
    city: Optional[str] = None
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)


class AddressUpdate(BaseModel):
    name: str | None = Field(None, min_length=1)
    city: Optional[str] = None
    latitude: Optional[float] = Field(None, ge=-90, le=90)
    longitude: Optional[float] = Field(None, ge=-180, le=180)


class AddressResponse(AddressCreate):
    id: int

    class Config:
        from_attributes = True