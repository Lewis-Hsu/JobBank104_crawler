from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MemberCenterPage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.frequency = 1
        self.wait = WebDriverWait(self.driver, self.timeout, self.frequency) 
        
    @property
    def get_user_name(self):
        # get user name
        user_name = self.driver.find_element(By.XPATH, "//*[@id=\"name_link\"]")

        return user_name.text

    def click_logout_btn(self):
        # click logout btn
        logout_button = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[@id=\"global_bk\"]/ul/li[2]/ul/li[5]/a")))
        logout_button.click()

        return self
