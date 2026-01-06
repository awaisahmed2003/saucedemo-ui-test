from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time

service = Service("C:/WebDriver/msedgedriver.exe")
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Edge(service=service, options=options)

# Test Case 1: Open Login Page
driver.get("https://www.saucedemo.com/")
assert "Swag Labs" in driver.page_source
time.sleep(3)

# Test Case 2: Valid Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)
assert "inventory" in driver.current_url

# Test Case 3: Add Item to Cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
assert cart_badge == "1"
time.sleep(3)

# Test Case 4: Go to Cart
driver.find_element(By.ID, "shopping_cart_container").click()
assert "cart" in driver.current_url
time.sleep(3)

# Test Case 5: Remove Item from Cart
driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

shopping_cart_badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
assert len(shopping_cart_badges) == 0

time.sleep(3)

# Test Case 4: Logout
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(3)
driver.find_element(By.ID, "logout_sidebar_link").click()
time.sleep(3)
assert "saucedemo.com" in driver.current_url

# Test Case 5: Invalid Login
driver.find_element(By.ID, "user-name").send_keys("wrong_user")
driver.find_element(By.ID, "password").send_keys("wrong_pass")
driver.find_element(By.ID, "login-button").click()
time.sleep(4)
error_msg = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']").text
assert "Username and password do not match" in error_msg

driver.quit()
