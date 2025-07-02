import logging
import inspect


class LogGenerator:
    @staticmethod
    def loggen():
        name = inspect.stack()[1][3]
        logger = logging.getLogger(name)
        logfile = logging.FileHandler("D://NOPCommerce//DemoNopCommerce//Logs//nopcommerce.log")
        logformat = logging.Formatter("%(asctime)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s ")
        logfile.setFormatter(logformat)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger
