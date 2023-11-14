import logging

class Logg:
    @staticmethod
    def log():
        logger=logging.getLogger()
        fhandler=logging.FileHandler(r"C:\Users\Hp\PycharmProjects\pythonProject\logs\noplog.log",mode='a')
        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger