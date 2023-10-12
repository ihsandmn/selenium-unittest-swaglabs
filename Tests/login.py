from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from PageObjects.loginpage import LoginPage


class TestHome(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install())
        )
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url = "https://saucedemo.com"

    # Testing Valid Login Page
    def test_loginPage(self):
        driver = self.driver
        driver.get(self.base_url)
        loginpage = LoginPage(driver)
        self.assertEqual("Swag Labs", self.driver.title, "Web title not matching")
        self.assertIsNotNone(loginpage.valid_login_page)

    # TC-1 Verify Login Successfully 1
    def test_login_1(self):
        driver = self.driver
        driver.get(self.base_url)
        loginpage = LoginPage(driver)
        loginpage.input_username_login("standard_user")
        loginpage.input_password_login("secret_sauce")
        loginpage.click_login_btn()
        self.assertIsNotNone(loginpage.valid_success_login)

    # TC-2 Verify Login Successfully 2
    def test_login_2(self):
        driver = self.driver
        driver.get(self.base_url)
        loginpage = LoginPage(driver)
        loginpage.input_username_login("problem_user")
        loginpage.input_password_login("secret_sauce")
        loginpage.click_login_btn()
        self.assertIsNotNone(loginpage.valid_success_login)

    # TC-3 Verify Login Successfully 3
    def test_login_3(self):
        driver = self.driver
        driver.get(self.base_url)
        loginpage = LoginPage(driver)
        loginpage.input_username_login("performance_glitch_user")
        loginpage.input_password_login("secret_sauce")
        loginpage.click_login_btn()
        self.assertIsNotNone(loginpage.valid_success_login)

    # TC-4 Verify Login Successfully 4
    def test_login_4(self):
        driver = self.driver
        driver.get(self.base_url)
        loginpage = LoginPage(driver)
        loginpage.input_username_login("error_user")
        loginpage.input_password_login("secret_sauce")
        loginpage.click_login_btn()
        self.assertIsNotNone(loginpage.valid_success_login)

    # TC-5 Verify Login Unsuccessfully (Valid Username and Password) || Severity: Major || Priority: High
    def test_login_5(self):
        driver = self.driver
        driver.get(self.base_url)
        loginpage = LoginPage(driver)
        loginpage.input_username_login("locked_out_user")
        loginpage.input_password_login("secret_sauce")
        loginpage.click_login_btn()
        # self.assertIsNotNone(loginpage.valid_success_login)
        self.assertTrue(loginpage.alert_message_error)

    # TC-6 Verify Login Unsuccessfully (Invalid Username and Valid Password)
    def test_login_6(self):
        driver = self.driver
        driver.get(self.base_url)
        loginpage = LoginPage(driver)
        loginpage.input_username_login("standard_admin")
        loginpage.input_password_login("secret_sauce")
        loginpage.click_login_btn()
        self.assertTrue(loginpage.alert_message_error)

    # TC-7 Verify Login Unsuccessfully (Valid Username and Invalid Password)
    def test_login_7(self):
        driver = self.driver
        driver.get(self.base_url)
        loginpage = LoginPage(driver)
        loginpage.input_username_login("standard_user")
        loginpage.input_password_login("secret_mustard")
        loginpage.click_login_btn()
        self.assertTrue(loginpage.alert_message_error)

    # TC-8 Verify Login Unsuccessfully (Invalid Username and Password)
    def test_login_8(self):
        driver = self.driver
        driver.get(self.base_url)
        loginpage = LoginPage(driver)
        loginpage.input_username_login("standard_rocks")
        loginpage.input_password_login("tomato_sauce")
        loginpage.click_login_btn()
        self.assertTrue(loginpage.alert_message_error)

    @classmethod
    def tearDown(self):
        self.driver.quit


if __name__ == "__main__":
    unittest.main()
