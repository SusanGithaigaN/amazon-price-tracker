from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
open_browser = webdriver.ChromeOptions()
open_browser.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=open_browser)

# driver.implicitly_wait(10)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# # find element
# statistics = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(statistics.text)

# search for an element
search = driver.find_element(By.NAME,"search")
# send keys from the keyboard to the search element
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# # automatically click link
# statistics.click()
driver.quit()
