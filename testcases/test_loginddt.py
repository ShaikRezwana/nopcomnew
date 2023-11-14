# import time
#
# import pytest
# from selenium import webdriver
# from pageObjects.loginpage import Loginpage
# from utilities.readProperties import ReadConfig
# from utilities.customLogger import LogGen
# from utilities import XLUtils
#
# class Test_002_DDT_Login:
#     baseurl = ReadConfig.getApplicationURL()
#     path=r"C:\\Users\\rezwana.shaik\\PycharmProjects\\nopcommerceapp\\TestData\\test excel.xlsx"
#     logger = LogGen.loggen()
#
#     def test_login(self,setup):
#         self.logger.info("***** Test_002_DDT_Login ******")
#         self.logger.info("**** Verifying test_login_ddt_test testcase******")
#         self.driver = setup
#         self.driver.get(self.baseurl)
#
#         self.lp = Loginpage(self.driver)
#
#         self.rows= XLUtils.getRowCount(self.path,sheet1)
#         print("Number of Rows in an Excel",self.rows)
#
#         lst_status=[]
#
#         for r in range(2,self.rows+1):
#             self.user = XLUtils.readData(self.path, 'sheet1', r, 1)
#             self.password = XLUtils.readData(self.path, 'sheet1', r, 2)
#             self.exp = XLUtils.readData(self.path, 'sheet1', r, 3)
#
#             self.lp.setUserName(self.user)
#             self.lp.setPassword(self.password)
#             self.lp.clickLogin()
#             time.sleep(5)
#
#             act_title=self.driver.title
#             exp_title="Dashboard / nopCommerce administration"
#
#             if act_title==exp_title:
#                 if self.exp=="Pass":
#                     self.logger.info("-----Test is pass----")
#                     self.lp.clicklogout()
#                     lst_status.append("Pass")
#                 elif self.exp=="Fail":
#                     self.logger.info("------Test is fail-----")
#                     self.lp.clicklogout()
#                     lst_status.append("Fail")
#             elif act_title!=exp_title:   #fail
#                 if self.exp == "Pass":
#                     self.logger.info("-----Test is Fail ----")
#                     lst_status.append("Fail")
#                 elif self.exp == "Fail":    #fail
#                     self.logger.info("------Test is pass-----")
#                     lst_status.append("Pass")   #both are fail so TC is pass
#             if "Fail" not in lst_status:
#                 self.logger.info("---------Login DDT test is passed--------")
#                 self.driver.close()
#                 assert True
#             else:
#                 self.logger.info("------------Login DDT test failed---------")
#                 self.driver.close()
#                 assert False
#         self.logger.info("--------End of Login DDT TC-----------")
#         self.logger.info("--------Completed TC_Login_DDT_002------")