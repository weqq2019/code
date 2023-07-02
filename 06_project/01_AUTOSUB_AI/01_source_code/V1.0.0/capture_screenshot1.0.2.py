import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image

# 定义一个类来封装浏览器自动化的操作
class BrowserAutomation:
    # 初始化方法，接收驱动路径作为参数
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None

    # 打开浏览器的方法
    def open_browser(self):
        service = Service(executable_path=self.driver_path)
        self.driver = webdriver.Chrome(service=service)

    # 打开本地HTML文件的方法
    def open_html(self, file_path):
        self.driver.get(f'file:///{file_path}')

    # 定位元素的方法
    def locate_element(self, by, value):
        return self.driver.find_element(by, value)

    # 截图的方法
    def capture_screenshot(self, screenshot_path):
        self.driver.save_screenshot(screenshot_path)

    # 关闭浏览器的方法
    def close_browser(self):
        self.driver.quit()

    # 截取元素的截图的方法
    def capture_element_screenshot(self, file_path, element_id):
        current_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        screenshot_path = f'06_project/01_AUTOSUB_AI/03_tests/Screenshots/element_screenshot_{current_datetime}.png'

        self.open_browser()
        self.open_html(file_path)
        element = self.locate_element(By.ID, element_id)
        location = element.location
        size = element.size
        self.capture_screenshot(screenshot_path)
        self.close_browser()
        self.crop_image(screenshot_path, location, size, screenshot_path)

    # 裁剪图片的静态方法
    @staticmethod
    def crop_image(image_path, location, size, cropped_image_path):
        image = Image.open(image_path)
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']
        cropped_image = image.crop((left, top, right, bottom))
        cropped_image.save(cropped_image_path)


# 使用类进行截图
driver_path = r'D:\BaiduSyncdisk\LQ\Code\M17\Code\03_utilities\chromedriver_win32\chromedriver.exe'
file_path = 'D:/BaiduSyncdisk/LQ/Code/M17/Code/06_project/01_AUTOSUB_AI/03_tests/example.html'
element_id = 'app'
# 创建BrowserAutomation类的实例
browser_automation = BrowserAutomation(driver_path)
# 调用实例的方法
browser_automation.capture_element_screenshot(file_path, element_id)
