import re
import requests
from zipfile import ZipFile
import os
import winreg


# 步骤 1: 获取本地浏览器版本
browser_version = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome'), 'DisplayVersion')[0]


# 步骤 2: 删除版本最后一部分
version_parts = browser_version.split('.')
version_parts.pop()  # 删除最后一部分
chrome_version = '.'.join(version_parts)

# 步骤 3: 获取最新版本的下载链接
release_url = f'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{chrome_version}'

response = requests.get(release_url)
latest_version = response.text.strip()

# 步骤 4: 下载 ChromeDriver
download_url = f'https://chromedriver.storage.googleapis.com/{latest_version}/chromedriver_win32.zip'

download_file = 'chromedriver_win32.zip'

download_path = os.path.join('06_project', '01_AUTOSUB_AI', '03_tests', 'download', download_file)


response = requests.get(download_url,download_path)
with open(download_file, 'wb') as file:
    file.write(response.content)

# 解压缩下载的文件
with ZipFile(download_path, 'r') as zip_file:
    zip_file.extractall(download_path)

# 清理下载的文件
os.remove(download_file)



