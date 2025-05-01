from .base import BaseBrowser
from euro_auto_radar.models.car import Car
from euro_auto_radar.models.car_filter import CarFilter
from typing import List
from selenium.webdriver.common.by import By

class StandVirtualBrowser(BaseBrowser):
    BASE_URL = "https://www.standvirtual.com/carros"

    def search(self, car_filter: CarFilter) -> List[Car]:
        self.navigate(self.BASE_URL)
        self.accept_cookies()
        if car_filter.make:
            self.select_make(car_filter.make)
            if car_filter.model:
                self.select_model(car_filter.model)
        if car_filter.year_from:
            self.select_year_of_registration_from(car_filter.year_from)
        if car_filter.year_to:
            self.select_year_of_registration_to(car_filter.year_to)

        self._get_and_move_to_element((By.XPATH, '//*[@data-testid="q"]')).click()

    def accept_cookies(self):
        accept_button = self._get_and_move_to_element((By.ID, 'onetrust-accept-btn-handler'))
        accept_button.click()

    def select_make(self, make_name):
        make_filter_locator = (By.XPATH, '//*[@data-testid="filter_enum_make"]')
        self._get_and_move_to_element(make_filter_locator).click()
        make_filter_el = self._get_and_move_to_element(make_filter_locator)
        for p in make_filter_el.find_elements(By.XPATH, './/p'):
            if make_name.lower() in p.text.lower():
                p.click()
                break
        make_arrow_el = make_filter_el.find_element(By.XPATH, './/*[@data-testid="arrow"]')
        make_arrow_el.click()

    def select_model(self, model_name):
        model_filter_locator = (By.XPATH, '//*[@data-testid="filter_enum_model"]')
        self._get_and_move_to_element(model_filter_locator).click()
        model_filter_el = self._get_and_move_to_element(model_filter_locator)
        for p in model_filter_el.find_elements(By.XPATH, './/p'):
            if model_name.lower() in p.text.lower():
                p.click()
                break
        model_arrow_el = model_filter_el.find_element(By.XPATH, './/*[@data-testid="arrow"]')
        model_arrow_el.click()
    
    def select_year_of_registration_from(self, year):
        year_filter_locator = (By.XPATH, '//*[@data-testid="filter_float_first_registration_year"]')
        year_filter_el = self._get_and_move_to_element(year_filter_locator)
        range_from_locator = (By.XPATH, './/input[@placeholder="Ano de"]')
        year_from_el = year_filter_el.find_element(*range_from_locator)
        year_from_el.click()
        year_from_el.send_keys(year)
    
    def select_year_of_registration_to(self, year):
        year_filter_locator = (By.XPATH, '//*[@data-testid="filter_float_first_registration_year"]')
        year_filter_el = self._get_and_move_to_element(year_filter_locator)
        range_to_locator = (By.XPATH, './/input[@placeholder="Ano até"]')
        year_to_el = year_filter_el.find_element(*range_to_locator)
        year_to_el.click()
        year_to_el.send_keys(year)
