import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import os

logging.basicConfig(level=logging.DEBUG)

class PageLoader:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')  # Run in headless mode

    def get_text_and_source_from_page(self, url):
        logging.debug("Entering get_text_and_source_from_page method")
        
        # Verify the ChromeDriver path
        if not os.path.exists(self.driver_path):
            raise FileNotFoundError(f"ChromeDriver not found at {self.driver_path}")

        # Set up the WebDriver
        service = Service(self.driver_path)
        logging.debug("Service created")
        
        driver = webdriver.Chrome(service=service, options=self.options)
        logging.debug("WebDriver created")
        
        try:
            # Navigate to the URL
            driver.get(url)
            logging.debug(f"Navigated to {url}")

            # Wait for the page to load completely (adjust the condition as needed)
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            logging.debug("Page loaded")

            # Optionally, wait for additional time to ensure all scripts have run
            time.sleep(5)

            # Fetch the page source
            page_source = driver.page_source

            # Parse the page source with BeautifulSoup
            soup = BeautifulSoup(page_source, 'html.parser')
            page_text = soup.get_text()
            return page_text, page_source
        finally:
            # Close the WebDriver
            driver.quit()
            # Close the Service
            service.stop()
            logging.debug("WebDriver and Service closed")

# Example usage
if __name__ == "__main__":
    driver_path = '/path/to/chromedriver'
    page_loader = PageLoader(driver_path)
    url = 'https://example.com'
    page_text, page_source = page_loader.get_text_and_source_from_page(url)
    print(page_text)