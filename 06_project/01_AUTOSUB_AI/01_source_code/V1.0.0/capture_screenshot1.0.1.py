import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image


def open_browser(driver_path):
    # 创建浏览器驱动实例
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    return driver


def open_html(driver, file_path):
    # 打开本地 HTML 文件
    driver.get(f'file:///{file_path}')


def locate_element(driver, by, value):
    # 定位要截图的元素
    return driver.find_element(by, value)


def capture_screenshot(driver, screenshot_path):
    # 执行截图操作
    driver.save_screenshot(screenshot_path)


def close_browser(driver):
    # 关闭浏览器
    driver.quit()


def crop_image(image_path, location, size, cropped_image_path):
    # 裁剪图像
    image = Image.open(image_path)
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    cropped_image = image.crop((left, top, right, bottom))
    cropped_image.save(cropped_image_path)


def capture_element_screenshot(driver_path, file_path, element_id):
    # 生成唯一的文件名
    current_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    screenshot_path = f'06_project/01_AUTOSUB_AI/03_tests/Screenshots/element_screenshot_{current_datetime}.png'

    # 打开浏览器
    driver = open_browser(driver_path)
    # 打开本地 HTML 文件
    open_html(driver, file_path)
    # 定位要截图的元素
    element = locate_element(driver, By.ID, element_id)
    location = element.location
    size = element.size
    # 执行截图操作
    capture_screenshot(driver, screenshot_path)
    # 关闭浏览器
    close_browser(driver)
    # 裁剪图像
    crop_image(screenshot_path, location, size, screenshot_path)


# 调用截图函数
driver_path = r'D:\BaiduSyncdisk\LQ\Code\M17\Code\03_utilities\chromedriver_win32\chromedriver.exe'
file_path = 'D:/BaiduSyncdisk/LQ/Code/M17/Code/06_project/01_AUTOSUB_AI/03_tests/example.html'
element_id = 'app'
capture_element_screenshot(driver_path, file_path, element_id)
