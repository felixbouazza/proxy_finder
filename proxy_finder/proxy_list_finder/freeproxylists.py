from driver import FirefoxProxyFinder
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pathlib import Path

class FreeProxyLists(FirefoxProxyFinder):

    def __init__(self, url):
        super().__init__()
        self.url = url
        self.driver.get(self.url)
        self.csv_file_path = Path.joinpath(self.data_dir_path, "freeproxylists.csv")

    def get_proxies(self):

        self.get_proxy_by_page()

        while next_page := self.get_next_page():
            next_page.click()
            self.get_proxy_by_page()
        
        self.write_data_to_csv()

    def get_proxy_by_page(self):
        
        self.wait_page_blocking('g-recaptcha')
        self.wait_page_blocking('vignette-creative-content')

        tables = self.driver.find_element(By.CLASS_NAME, "DataGrid")

        odds = tables.find_elements(By.CLASS_NAME, 'Odd')
        evens = tables.find_elements(By.CLASS_NAME, 'Even')

        for odd in odds:
            td = odd.find_element(By.TAG_NAME, 'td')
            try:
                link = td.find_element(By.TAG_NAME, 'a')
                self.proxies.add(link.text)
            except NoSuchElementException:
                ...

        for even in evens:
            td = even.find_element(By.TAG_NAME, 'td')
            try:
                link = td.find_element(By.TAG_NAME, 'a')
                self.proxies.add(link.text)
            except NoSuchElementException:
                ...
    
    def get_next_page(self):
        page_number_list = self.driver.find_elements(By.CLASS_NAME, "page")

        page_number_list_first = page_number_list[0]

        pages = page_number_list_first.find_elements(By.TAG_NAME, "a")
        for page in pages:
            if "Suivant" in page.text:
                return page
        return False
