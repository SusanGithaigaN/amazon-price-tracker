from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Pass config to webdriver
driver = webdriver.Chrome(options=chrome_options)

# Set an implicit wait to wait for a maximum of 10 seconds for elements to be present
driver.implicitly_wait(10)

# Navigate to the page
driver.get('https://www.python.org/')

# Find elements by css selector
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

# Create events dictionary
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)

driver.quit()
