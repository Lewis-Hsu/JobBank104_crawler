from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.frequency = 1
        self.wait = WebDriverWait(self.driver, self.timeout, self.frequency)

    def click_login_btn(self):

        self.driver.get("https://www.104.com.tw/jobs/main/")

        # click account btn
        login_button = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id=\"global_bk\"]/ul/li[2]/ul/li[6]/a")))
        login_button.click()

        return self

    def click_name_btn(self):
        # click user name
        name_button = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id=\"name_link\"]")))
        name_button.click()

        return self

    def click_member_center_btn(self):
        # click user name
        name_button = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id=\"global_bk\"]/ul/li[2]/ul/li[4]/ul/li/div/dl/dt[1]/a")))
        name_button.click()

        return self
