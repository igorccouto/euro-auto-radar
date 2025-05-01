from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class CarFilter:
    make: Optional[str] = None
    model: Optional[str] = None
    year_from: Optional[int] = None
    year_to: Optional[int] = None
    price_from: Optional[float] = None
    price_to: Optional[float] = None
    mileage_from: Optional[int] = None
    mileage_to: Optional[int] = None
    fuel_types: List[str] = field(default_factory=list)

    def matches(self, car) -> bool:
        if self.make and self.make.lower() != car.make.lower():
            return False
        if self.model and self.model.lower() != car.model.lower():
            return False
        if self.year_from and car.first_registration_year < self.year_from:
            return False
        if self.year_to and car.first_registration_year > self.year_to:
            return False
        if self.price_from and car.price < self.price_from:
            return False
        if self.price_to and car.price > self.price_to:
            return False
        if self.mileage_from and car.mileage < self.mileage_from:
            return False
        if self.mileage_to and car.mileage > self.mileage_to:
            return False
        if self.fuel_types and car.fuel_type.lower() not in [ft.lower() for ft in self.fuel_types]:
            return False
        return True
