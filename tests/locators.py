from selenium.webdriver.common.by import By


USERNAME = (By.XPATH, "//input[@id='email']")
PASSWORD = (By.XPATH, "//input[@id='password']")
LOGIN_BUTTON = (By.XPATH, "//div[@id='app']/div/main/div/form/button/span")
DOWNLOAD_BUTTON = (By.XPATH, "//div[@id='app']/div/main/div/div/div[2]/button/span/p")