from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Create a new instance of the Chrome driver
driver = webdriver.Chrome('./chromedriver')
# Open the e-learning platform
driver.get("https://www.your-elearning-platform.com")
# Verify the page title
assert "E-Learning" in driver.title
# Locate the login form and perform login
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
username.send_keys("testuser")
password.send_keys("testpassword")
password.send_keys(Keys.RETURN)
# Verify successful login
assert "Dashboard" in driver.title
# Close the browser
driver.quit()