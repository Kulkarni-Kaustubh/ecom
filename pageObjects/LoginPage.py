from selenium import webdriver

class LoginPage:
    textbox_username_id = "Email"
    textbox_pasword_id = "Password"
    button_login_xpath = "//input[@class='button-1 login-button']"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def setusername(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element_by_id(self.textbox_pasword_id).clear()
        self.driver.find_element_by_id(self.textbox_pasword_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).clck()

    def clicklogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()
