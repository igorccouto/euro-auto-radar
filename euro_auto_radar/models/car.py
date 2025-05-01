from dataclasses import dataclass, field
from typing import Optional

@dataclass(order=True)
class Car:
    make: str
    model: str
    mileage: int
    first_registration_year: int
    price: float
    source: str
    url: str
    fuel_type: str
    transmission: str
    horsepower: Optional[int] = None
    location: Optional[str] = None
    vat_deductible: Optional[bool] = None
    extra: dict = field(default_factory=dict)

    def __post_init__(self):
        self.make = self.make.title()
        self.model = self.model.title()

    def to_dict(self):
        return self.__dict__
