from logging import getLogger, basicConfig, FileHandler, StreamHandler, DEBUG, ERROR

def logger_config():

    logger = getLogger()

    data_format = '%(asctime)s : %(name)s : %(levelname)s : %(message)s'

    file_handler = FileHandler('data.log', mode='w')

    console_handler = StreamHandler()

    file_handler.setLevel(DEBUG)

    console_handler.setLevel(ERROR)

    basicConfig(level=DEBUG, format=data_format, handlers=[file_handler, console_handler])

    return logger
