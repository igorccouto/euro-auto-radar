from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Optional

class BaseBrowser:
    def __init__(self, headless: bool = True):
        self.driver: Optional[WebDriver] = None
        self.headless = headless

    def create_driver(self):
        options = Options()
        if self.headless:
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=options)

    def close_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None

    def navigate(self, url: str):
        if not self.driver:
            self.create_driver()
        self.driver.get(url)

    def __enter__(self):
        self.create_driver()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_driver()
