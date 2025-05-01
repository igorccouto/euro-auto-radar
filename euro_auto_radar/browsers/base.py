from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Optional

class BaseBrowser:
    def __init__(self, headless: bool = True, default_timeout: int = 10):
        self.driver = self._create_driver(headless)
        self.wait = WebDriverWait(self.driver, default_timeout)

    def close_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None

    def navigate(self, url: str):
        self.driver.get(url)

    def _create_driver(self, headless):
        options = Options()
        if headless:
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        return webdriver.Chrome(options=options)
    def _element_in_viewport(self, locator):
        element = self.driver.find_element(*locator)
        return self.driver.execute_script("""
            var elem = arguments[0],
                box = elem.getBoundingClientRect(),
                cx = box.left + box.width / 2,
                cy = box.top + box.height / 2,
                e = document.elementFromPoint(cx, cy);
            for (; e; e = e.parentElement) {
                if (e === elem)
                    return true;
            }
            return false;
        """, element)

    def _get_and_move_to_element(self, locator, expected_condition=EC.presence_of_element_located, parent_element=None):
        search_context = parent_element if parent_element is not None else self.driver
        def find_in_context(driver):
            return expected_condition(locator)(search_context)
        element = self.wait.until(find_in_context)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait.until(lambda d: self._element_in_viewport(locator) if parent_element is None else self._element_in_viewport_within(locator, parent_element))
        return element

    def __enter__(self):
        self.create_driver()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_driver()
