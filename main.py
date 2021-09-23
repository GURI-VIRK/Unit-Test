from selenium import webdriver
import time
import unittest

class Logintest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome('./chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver=self.driver

        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        login= Loginpage(driver)
        login.enter_user("Admin")
        login.enter_pass("admin123")
        login.click_login_btn()
        time.sleep(2)
        homepage=Homepage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        time.sleep(2)
        # self.driver.find_element_by_id('txtUsername').send_keys("Admin")
        # self.driver.find_element_by_id('txtPassword').send_keys("admin123")
        # self.driver.find_element_by_class_name('button').click()
        # time.sleep(2)
        # self.driver.find_element_by_link_text('Welcome Abhishek').click()
        # self.driver.find_element_by_link_text("Logout").click()
        # time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

class Loginpage():

    def __init__(self,driver):
        self.driver= driver

        self.username_textbox_id="txtUsername"
        self.password_textbox_id = "txtPassword"
        self.login_button_class_name = "button"

    def enter_user(self,username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_pass(self,password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login_btn(self):
        self.driver.find_element_by_class_name(self.login_button_class_name).click()


class Homepage():
    def __init__(self,driver):
        self.driver= driver

        self.welcome_link_text = "Welcome Paul"
        self.logout_link_text = "Logout"

    def click_welcome(self):
        self.driver.find_element_by_link_text(self.welcome_link_text).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_text).click()
