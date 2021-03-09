import inspect
import logging.config

def Logger(logLevel=logging.DEBUG):
    # this gets the name of current class (from where the method is called)
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("automation.log", "w")
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter("%(asctime)s: %(name)s: - %(levelname)s %(message)s",
                                  datefmt="%m/%d/%Y %I:%M:%S %p")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return  logger