from .base import BaseBrowser
from euro_auto_radar.models.car import Car
from euro_auto_radar.models.car_filter import CarFilter
from typing import List

class StandVirtualBrowser(BaseBrowser):
    BASE_URL = "https://www.standvirtual.com/carros"

    def search(self, car_filter: CarFilter) -> List[Car]:
        pass
