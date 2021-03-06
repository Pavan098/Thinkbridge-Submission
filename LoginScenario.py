from selenium import webdriver
from selenium.webdriver.common.by import By

# launch new browser
driver = webdriver.Chrome(executable_path="F:\\chromedriver\\chromedriver.exe")
driver.implicitly_wait(10)

# Open URL
driver.get("https://jt-dev.azurewebsites.net/#/SignUp")
print(driver.title)

# validate the dropdown has English and Dutch left
english = "English"
dutch = "Dutch"
driver.implicitly_wait(20)
driver.find_element(By.XPATH, "//div[@placeholder='Choose Language']").is_enabled()
driver.find_element(By.XPATH, "//div[@placeholder='Choose Language']").click()
driver.find_element(By.XPATH, "//div[contains(text(),'"+english+"')]").is_enabled()
print(driver.find_element(By.XPATH, "//div[contains(text(),'"+english+"')]").text)
driver.find_element(By.XPATH, "//div[contains(text(),'"+dutch+"')]").is_enabled()
print(driver.find_element(By.XPATH, "//div[contains(text(),'"+dutch+"')]").text)

# fill the name in the full name and organization as well
# Input your email address
driver.find_element(By.ID, "name").send_keys("Classmate")
driver.implicitly_wait(20)
driver.find_element(By.ID, "orgName").send_keys("Classmate")
driver.find_element(By.ID, "singUpEmail").send_keys("Classmate@gmail.com")

# Click on I agree to the terms conditions
driver.find_element(By.XPATH, "//span[contains(text(),'I agree to the')]").click()
driver.implicitly_wait(10)

# Click on SignUp
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Validate you receive the email
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//span[contains(text(),'A welcome email has been sent. Please check your email')]")\
    .is_displayed()

# print the message you get
print(driver.find_element(By.XPATH, "//span[contains(text(),'A welcome email has been sent. Please check your email')]")
      .text)

driver.implicitly_wait(10)

# close the browser
driver.quit()

