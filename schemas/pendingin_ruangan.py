from pydantic import BaseModel, Field
from typing import Optional

class PendinginRuanganBase(BaseModel):
    model: str = Field(..., title="Model Pendingin Ruangan", max_length=100)
    brand: str = Field(..., title="Merek Pendingin Ruangan", max_length=100)
    capacity: int = Field(..., title="Kapasitas Pendingin Ruangan (BTU)", ge=0)
    energy_rating: float = Field(..., title="Rating Energi Pendingin Ruangan", ge=0.0, le=5.0)
    price: float = Field(..., title="Harga Pendingin Ruangan", ge=0.0)
    availability: bool = Field(..., title="Ketersediaan Pendingin Ruangan")

class PendinginRuanganCreate(PendinginRuanganBase):
    pass

class PendinginRuanganUpdate(PendinginRuanganBase):
    model: Optional[str] = Field(None, title="Model Pendingin Ruangan", max_length=100)
    brand: Optional[str] = Field(None, title="Merek Pendingin Ruangan", max_length=100)
    capacity: Optional[int] = Field(None, title="Kapasitas Pendingin Ruangan (BTU)", ge=0)
    energy_rating: Optional[float] = Field(None, title="Rating Energi Pendingin Ruangan", ge=0.0, le=5.0)
    price: Optional[float] = Field(None, title="Harga Pendingin Ruangan", ge=0.0)
    availability: Optional[bool] = Field(None, title="Ketersediaan Pendingin Ruangan")

class PendinginRuanganInDBBase(PendinginRuanganBase):
    id: int = Field(..., title="ID Pendingin Ruangan")

    class Config:
        orm_mode = True

class PendinginRuangan(PendinginRuanganInDBBase):
    pass

class PendinginRuanganInDB(PendinginRuanganInDBBase):
    pass
