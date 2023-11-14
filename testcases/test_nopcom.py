from selenium import webdriver
import pytest
from pageobjects.login import login
from utilities.readproperties import Readconfig
from utilities.customerlogger import Logg

class Test_001_nop:
    baseurl=Readconfig.getapplicationurl()
    username=Readconfig.enterusename()
    password=Readconfig.enterpassword()

    logger=Logg.log()

    @pytest.mark.sanity
    def test_loggedin(self,setup):
        self.logger.info("******** Started logging function ***********")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("********* Logged in successfully ******")
        self.driver.close()

    @pytest.mark.sanity
    def test_title(self,setup):
        self.logger.info("***** Title of the page ********")
        self.driver=setup
        self.driver.get(self.baseurl)
        act_title=self.driver.title
        print(act_title)
        if act_title=="Your store. Login":
            assert True
            self.logger.info("***** Page title is printed")
        else:
            self.driver.save_screenshot(r"C:\\Users\\Hp\\PycharmProjects\\pythonProject\\screenshots\\" + "test_title.png")
            self.logger.error("********** page title failed to match **********")
            assert False
            self.driver.close()
