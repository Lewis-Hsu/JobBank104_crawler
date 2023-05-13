from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from configurations.config import JobBank104Config
from page_object.job_bank_104.main import MainPage
from page_object.job_bank_104.login import LoginPage
from page_object.job_bank_104.member_center import MemberCenterPage


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
        LoginPage(self.driver).enter_user_name().enter_password().click_login_btn()

    def get_user_name(self):

        MainPage(self.driver).click_name_btn().click_member_center_btn()
        return MemberCenterPage(self.driver).get_user_name
        
    def logout(self):   

        MemberCenterPage(self.driver).click_logout_btn()


if __name__ == "__main__":

    driver = create_driver()
    job_bank_104 = JobBank104(driver)

    try:
        job_bank_104.login()
    except Exception:
        print("login failed")

    try:
        user_name = job_bank_104.get_user_name()
        assert user_name == JobBank104Config.UserInfo.name
        
    except Exception:
        print("get user name failed")


    try:
        job_bank_104.logout()
    except Exception:
        print("logout failed")

    driver.quit()
