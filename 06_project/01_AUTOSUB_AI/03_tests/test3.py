import re
from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建一个Chrome浏览器实例
browser = webdriver.Chrome()


# 获取ChromeDriver版本
browser.get('chrome://version')
version_element = browser.find_element(By.XPATH, '//td[contains(text(), "ChromeDriver")]')
version_text = version_element.text
version_match = re.search(r'ChromeDriver\s+(\d+\.\d+\.\d+\.\d+)', version_text)
if version_match:
    chromedriver_version = version_match.group(1)
    print("ChromeDriver版本：", chromedriver_version)
else:
    print("无法获取ChromeDriver版本")

# # 关闭浏览器实例
# browser.quit()
