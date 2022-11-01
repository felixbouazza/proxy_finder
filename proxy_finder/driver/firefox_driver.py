from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import csv
from pathlib import Path


class FirefoxProxyFinder:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.home_path = Path.home()
        self.data_dir_path = Path.joinpath(self.home_path, "data/csv")
        self.csv_file_path = None
        self.proxies = set()
    
    def wait_page_blocking(self, class_name):
        if class_name == "vignette-creative-content":
            self.skip_google_ad()
        while True:
            try:
                self.driver.find_element(By.CLASS_NAME, class_name)
            except NoSuchElementException:
                break
        time.sleep(5)
    
    def skip_google_ad(self):
        try:
            dismiss_button = self.driver.find_element(By.CLASS_NAME, "dismiss-button")
            dismiss_button.click()
        except NoSuchElementException:
            ...
    
    def get_proxies(self):
        ...
    
    def get_proxy_by_page(self):
        ...
    
    def get_next_page(self):
        ...

    def write_data_to_csv(self):
        with open(self.csv_file_path, 'w') as csv_file:
            fieldnames = ["IP"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for proxy in self.proxies:
                writer.writerow({"IP": proxy})