from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


# Extracting email and password saved in auth.txt file
with open('auth.txt', 'r') as file:
    lines = file.read().split('/')

email = lines[0]
password = lines[1]

# Chrome Option to click on block for browser notification pop up
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://www.facebook.com/")

element = driver.find_element(By.ID, "email")
element.send_keys(email)
element = driver.find_element(By.ID, "pass")
element.send_keys(password)
element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button")
element.click()

wait = WebDriverWait(driver, 20)

# Explicit wait for Home button to clickable
element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[2]/div[3]/div/div[1]/div[1]/ul/li[1]/span/div/a")))
element.click()

# Explicit wait for Create Post button to clickable
element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span")))
element.click()

sleep(5)
driver.switch_to.active_element.send_keys("What a nice day.")

# Explicit wait for Post button to clickable
element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div[3]/div[2]/div")))
element.click()

sleep(10)
driver.get("https://www.facebook.com/deepak.bishi.5")

sleep(5)
# Clcik on add friend button
element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[1]/div/div/div/div/div/div/div/div[2]/div")))
element.click()

# Click on message button
element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/div/div/div[2]/div/div/div[1]/div/div")))
element.click()

# Send message in textbox
element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div")))
element.send_keys("Hey")

# Click on send button
element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[1]/div[5]/div[1]/div[1]/div[1]/div/div/div/div/div/div/div[2]/div/div[2]/form/div/div[3]/span[2]/div")))
element.click()
