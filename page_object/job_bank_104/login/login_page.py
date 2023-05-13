from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from configurations.config import JobBank104Config

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.frequency = 1
        self.wait = WebDriverWait(self.driver, self.timeout, self.frequency)
        self.user = JobBank104Config.UserInfo.user
        self.password = JobBank104Config.UserInfo.password

    def enter_user_name(self):
        # enter user name
        user_input = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id=\"username\"]")))
        user_input.clear()
        user_input.send_keys(self.user)

        return self
    
    def enter_password(self):
        # enter password
        password_input = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id=\"password\"]")))
        password_input.clear()
        password_input.send_keys(self.password)
        
        return self

    def click_login_btn(self):
        # click login btn
        submit_button = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id=\"submitBtn\"]")))
        submit_button.click()

        return self
