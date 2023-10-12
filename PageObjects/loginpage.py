from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def valid_login_page(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".login_logo")

    def input_username_login(self, data):
        return self.driver.find_element(By.NAME, "user-name").send_keys(data)

    def input_password_login(self, data):
        return self.driver.find_element(By.NAME, "password").send_keys(data)

    def click_login_btn(self):
        return self.driver.find_element(By.NAME, "login-button").click()

    def valid_success_login(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".inventory_list")

    def alert_message_error(self):
        return self.driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
