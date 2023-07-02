import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image

def capture_screenshot():
    # 指定浏览器驱动路径
    driver_path = Service(executable_path=r'D:\BaiduSyncdisk\LQ\Code\M17\Code\03_utilities\chromedriver_win32\chromedriver.exe') 
    
    # 创建浏览器驱动实例
    driver = webdriver.Chrome(service=driver_path)

    # 打开本地 HTML 文件
    driver.get('file:///D:/BaiduSyncdisk/LQ/Code/M17/Code/06_project/01_AUTOSUB_AI/03_tests/example.html')

    # 定位要截图的元素
    element = driver.find_element(By.ID, 'app')  # 使用元素的 ID 定位元素

    # 获取元素的位置和大小
    location = element.location
    size = element.size

    # 执行截图操作
    screenshot_path = '06_project/01_AUTOSUB_AI/03_tests/Screenshots/screenshot2.png'
    driver.save_screenshot(screenshot_path)

    # 使用二进制模式打开截图文件
    with open(screenshot_path, 'rb') as f:
        image = Image.open(f)
        cropped_image = image.crop((location['x'], location['y'], location['x'] + size['width'], location['y'] + size['height']))

    # 保存裁剪后的图像
    # 生成唯一的文件名
    # 获取当前日期
    current_datetime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    
    cropped_image.save(f'06_project/01_AUTOSUB_AI/03_tests/Screenshots/element_screenshot_{current_datetime}.png')

    # 关闭浏览器
    driver.quit()
    

# 调用截图函数
capture_screenshot()
