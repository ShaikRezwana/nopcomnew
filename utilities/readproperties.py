import configparser

config=configparser.RawConfigParser()
config.read(r"C:\Users\Hp\PycharmProjects\pythonProject\configurations\config.ini")

class Readconfig:
    @staticmethod
    def getapplicationurl():
        url=config.get("details","baseurl")
        return url

    @staticmethod
    def enterusename():
        username=config.get("details","username")
        return username

    @staticmethod
    def enterpassword():
        password=config.get("details","password")
        return password
