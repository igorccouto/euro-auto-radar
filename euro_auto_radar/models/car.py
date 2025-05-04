from dataclasses import dataclass, field
from typing import Optional

@dataclass(order=True)
class Car:
    id: str
    make: str
    model: str
    edition: str
    mileage: int
    price: float
    source: str
    url: str
    first_registration_year: str
    first_registration_month: Optional[str] = None
    fuel_type: Optional[str] = None
    transmission: Optional[str] = None
    horsepower: Optional[int] = None
    location: Optional[str] = None
    vat_deductible: Optional[bool] = None
    extra: dict = field(default_factory=dict)

    def __post_init__(self):
        self.make = self.make.title()
        self.model = self.model.title()

    def to_dict(self):
        return self.__dict__
