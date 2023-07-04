import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image
from log import MyLogger

# 创建一个日志对象
logger = MyLogger('screenshot')

class Browser:
    def __init__(self, driver_path):
        """
        初始化浏览器对象。

        Args:
            driver_path (str): 浏览器驱动程序的路径。
        """
        self.driver_path = driver_path
        self.driver = None

    def open(self):
        """
        打开浏览器。
        """
        service = Service(executable_path=self.driver_path)
        self.driver = webdriver.Chrome(service=service)

    def close(self):
        """
        关闭浏览器。
        """
        self.driver.quit()


class Element:
    def __init__(self, driver):
        """
        初始化元素定位对象。

        Args:
            driver: 浏览器驱动程序对象。
        """
        self.driver = driver

    def locate(self, by, value):
        """
        定位元素。

        Args:
            by: 定位方式。
            value: 定位值。

        Returns:
            WebElement: 定位到的元素对象。
        """
        return self.driver.find_element(by, value)


class Screenshot:
    @staticmethod
    def capture(driver, screenshot_path):
        """
        截取屏幕截图。

        Args:
            driver: 浏览器驱动程序对象。
            screenshot_path (str): 截图保存路径。
        """
        driver.save_screenshot(screenshot_path)

    @staticmethod
    def crop(image_path, location, size, cropped_image_path):
        """
        裁剪图像。

        Args:
            image_path (str): 原始图像路径。
            location (dict): 元素位置。
            size (dict): 元素尺寸。
            cropped_image_path (str): 裁剪后图像保存路径。
        """
        image = Image.open(image_path)
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        cropped_image = image.crop((left, top, right, bottom))
        cropped_image.save(cropped_image_path)


class BrowserAutomation:
    def __init__(self, driver_path):
        """
        初始化浏览器自动化对象。

        Args:
            driver_path (str): 浏览器驱动程序的路径。
        """
        self.browser = Browser(driver_path)

    def capture_element_screenshot(self, file_path, element_id, screenshot_path):
        """
        截取指定元素的屏幕截图。

        Args:
            file_path (str): HTML文件路径。
            element_id (str): 元素的ID。
            screenshot_path (str): 截图保存路径。
        """
        # 获取当前日期时间作为截图文件名
        current_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        screenshot_path = f'{screenshot_path}/element_screenshot_{current_datetime}.png'

        # 打开浏览器
        self.browser.open()
        driver = self.browser.driver
        driver.get(f'file:///{file_path}')

        # 定位元素
        element = Element(driver).locate(By.ID, element_id)
        location = element.location
        size = element.size

        # 截取屏幕截图
        Screenshot.capture(driver, screenshot_path)

        # 关闭浏览器
        self.browser.close()

        # 裁剪图像
        Screenshot.crop(screenshot_path, location, size, screenshot_path)

        logger.info('成功截取了屏幕截图')
