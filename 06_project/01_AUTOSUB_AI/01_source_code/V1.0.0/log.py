import logging
from config import LOG_LEVEL


class MyLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(LOG_LEVEL)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # 创建一个文件处理器，并设置格式
        file_handler = logging.FileHandler(
            '06_project/01_AUTOSUB_AI/01_source_code/V1.0.0/logs/app.log',
            encoding='utf-8')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

        # 创建一个控制台处理器，并设置格式
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
