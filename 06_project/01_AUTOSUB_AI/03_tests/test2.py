import datetime
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image
# from log import MyLogger



# # 创建一个日志对象
# logger = MyLogger('screenshot')

class Browser:
    def __init__(self, driver_path):
        self.driver_path = driver_path
        self.driver = None


    def open(self):
        service = Service(executable_path=self.driver_path)
        self.driver = webdriver.Chrome(service=service)
        
    def open_url(self, url):
        self.driver.get(url)

    def close(self):
        self.driver.quit()
        
        
        
driver_path = r'D:\BaiduSyncdisk\LQ\Code\M17\Code\06_project\01_AUTOSUB_AI\01_source_code\download\chromedriver.exe'
print(os.path.exists(driver_path))
    # 创建Browser对象，传入驱动程序路径
browser = Browser(driver_path=driver_path)  # 你需要将路径替换为实际的驱动程序路径

# 打开浏览器
browser.open()
# 打开网页
browser.open_url("https://www.baidu.com")

# 进行其他操作，例如访问网页、查找元素等

# 关闭浏览器
# browser.close()

while True:
    pass