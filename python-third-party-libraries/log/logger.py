import logging


class Logger:
    """
    异常信息log
    """

    # create logger
    __logger_name = "python_demo"
    __logger = logging.getLogger(__logger_name)
    __logger.setLevel(logging.DEBUG)

    # create file handler
    __log_path = "./log.log"
    __fileHandler = logging.FileHandler(__log_path)
    __fileHandler.setLevel(logging.DEBUG)

    # create formatter
    __fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d \n %(message)s"
    __datefmt = "%a %d %b %Y %H:%M:%S"
    __formatter = logging.Formatter(__fmt, __datefmt)

    # add handler and formatter to logger
    __fileHandler.setFormatter(__formatter)
    __logger.addHandler(__fileHandler)

    # print log info
    def debug(self, exception):
        self.__logger.debug(repr(exception))

    def info(self, exception):
        self.__logger.info(repr(exception))

    def warn(self, exception):
        self.__logger.warning(repr(exception))

    def error(self, exception):
        self.__logger.error(repr(exception))

    def critical(self, exception):
        self.__logger.critical(repr(exception))
