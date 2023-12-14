from selenium import webdriver

# keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# pass config to webdriver
driver= webdriver.Chrome(options=chrome_options)
# get the driver to open up a webpage
driver.get("https://amazon.com")


# close
# driver.close()
# shut down the entire browser
driver.quit()


# difference between ln 13 &15
# close(): just closes a single active tab
# quit(): quits the entire browser, ie closes all tabs