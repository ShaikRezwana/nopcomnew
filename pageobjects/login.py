class login:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    btn_login_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element("id", self.textbox_username_id).clear()
        self.driver.find_element("id", self.textbox_username_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element("id", self.textbox_password_id).clear()
        self.driver.find_element("id", self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element("xpath", self.btn_login_xpath).click()


