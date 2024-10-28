from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (make sure to have ChromeDriver installed and in your PATH)
service = Service('/Users/michaelleonard/slalom/ask-about/Selenium.WebDriver.ChromeDriver.130.0.6723.6900/driver/mac64/chromedriver')  # Update with the path to your ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in headless mode
driver = webdriver.Chrome(service=service, options=options)
url = 'https://hackathon.slalom.com/'
local_domain = 'hackathon.slalom.com'

try:
    # Navigate to the URL
    driver.get(url)

    # Wait for the page to load completely (adjust the condition as needed)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Optionally, wait for additional time to ensure all scripts have run
    time.sleep(5)

    # Fetch the page source
    page_source = driver.page_source

    # Write the page source to a file
    with open('text/'+local_domain+'/'+url[8:].replace("/", "_") + ".txt", "w") as f:
        f.write(page_source)
finally:
    # Close the WebDriver
    driver.quit()