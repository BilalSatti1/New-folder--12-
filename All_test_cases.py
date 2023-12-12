from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Chrome Options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


# test case 1 register for event
driver.get('http://65.0.134.88/')
driver.maximize_window()


driver.find_element(By.XPATH, '//input[@name="full_name"]').send_keys('bilal')
driver.find_element(By.XPATH, '//input[@name="email"]').send_keys('bilal@gmail.com')
driver.find_element(By.XPATH, '//input[@name="mobile"]').send_keys('1234567890')
driver.find_element(By.XPATH, '//input[@name="college"]').send_keys('punjab')
driver.find_element(By.XPATH, '//input[@name="branch"]').send_keys('d9')


driver.find_element(By.XPATH, '//input[@value="Register"]').click()

#test case 2 invalid login
driver.find_element(By.XPATH, '//a[@href="login.php"]').click()


driver.find_element(By.XPATH, '//input[@name="Username"]').send_keys('asd')

driver.find_element(By.XPATH, '//input[@name="Password"]').send_keys('abc12345')
driver.find_element(By.XPATH, '//input[@value="Login"]').click()
time.sleep(2)
#test case 3 valid login
driver.find_element(By.XPATH, '//input[@name="Username"]').send_keys('bilal')

driver.find_element(By.XPATH, '//input[@name="Password"]').send_keys('hassan123')
driver.find_element(By.XPATH, '//input[@value="Login"]').click()
time.sleep(3)

#test case 4 update
driver.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click()
time.sleep(2)

driver.find_element(By.XPATH, '//input[@name="branch"]').send_keys('a5')

driver.find_element(By.XPATH, '//input[@value="Update"]').click()
time.sleep(2)

#test case 5 delete
driver.find_element(By.XPATH, '//button[@class="btn btn-danger"]').click()

time.sleep(2)


#test case 6 logout
driver.find_element(By.XPATH, '//a[@href="logout.php"]').click()
