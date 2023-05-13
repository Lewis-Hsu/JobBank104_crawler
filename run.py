from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from page_object.job_bank_104.main import MainPage
from page_object.job_bank_104.login import LoginPage


def create_driver(headless=False):
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")

    driver = Chrome(ChromeDriverManager().install(), options=chrome_options)

    return driver


class JobBank104:

    def __init__(self, driver):
        self.driver = driver

    def login(self):

        MainPage(self.driver).click_login_btn()
        LoginPage(self.driver).enter_user_name(
        ).enter_password().click_login_btn()

    def get_user_name(self):

        MainPage(self.driver).click_name_btn().click_member_center_btn()


if __name__ == "__main__":
    driver = create_driver()

    job_bank_104 = JobBank104(driver)
    job_bank_104.login()
    job_bank_104.get_user_name()

    driver.quit()
