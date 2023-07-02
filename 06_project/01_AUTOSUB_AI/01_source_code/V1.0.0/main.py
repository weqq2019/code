from config import driver_path, file_path, element_id, screenshot_path
from capture_screenshot_1_0_4 import BrowserAutomation
from log import MyLogger
from config import LOG_LEVEL

# 创建一个日志对象
logger = MyLogger('main')


def main():
    # 设置日志级别
    logger.logger.setLevel(LOG_LEVEL)

    logger.debug('调试日志消息')
    logger.info('信息日志消息')
    logger.warning('警告日志消息')

    # 创建BrowserAutomation类的实例
    browser_automation = BrowserAutomation(driver_path)

    # 调用实例的方法进行截图
    browser_automation.capture_element_screenshot(file_path, element_id, screenshot_path)


if __name__ == "__main__":
    main()
