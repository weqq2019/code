import requests
from zipfile import ZipFile
import os
import winreg

class ChromeDriverDownloader:
    def __init__(self):
        self.download_dir = self.create_download_folder()

        
    def create_download_folder(self):
        # 获取当前工作目录
        current_path = os.path.abspath(os.path.dirname(__file__))
        # 创建 "download" 文件夹路径
        download_path = os.path.join(current_path, "download")

        # 如果 "download" 文件夹不存在，则创建它
        if not os.path.exists(download_path):
            os.makedirs(download_path)
        return download_path
   
    def get_browser_version(self):
        # 步骤 1: 获取本地浏览器版本
        browser_version = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                                             'SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome'),
                                              'DisplayVersion')[0]
        return browser_version

    def get_chrome_version(self, browser_version):
        # 步骤 2: 删除版本最后一部分
        version_parts = browser_version.split('.')
        version_parts.pop()  # 删除最后一部分
        chrome_version = '.'.join(version_parts)
        return chrome_version

    def get_download_url(self, chrome_version):
        # 步骤 3: 获取最新版本的下载链接
        release_url = f'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{chrome_version}'
        response = requests.get(release_url)
        latest_version = response.text.strip()
        download_url = f'https://chromedriver.storage.googleapis.com/{latest_version}/chromedriver_win32.zip'
        return download_url

    def download_chromedriver(self, download_url):
        # 步骤 4: 下载 ChromeDriver
        download_file = 'chromedriver_win32.zip'
        download_path = os.path.join(self.download_dir, download_file)

    

        response = requests.get(download_url)
        with open(download_path, 'wb') as file:
            file.write(response.content)

        return download_path

    def extract_chromedriver(self, download_path):
        # 解压缩下载的文件
        with ZipFile(download_path, 'r') as zip_file:
            zip_file.extractall(self.download_dir)

    def clean_up(self, download_path):
        # 清理下载的文件
        os.remove(download_path)

    def download_chromedriver_for_current_browser(self):
        # 获取浏览器版本
        browser_version = self.get_browser_version()
        # 获取 Chrome 版本
        chrome_version = self.get_chrome_version(browser_version)
        # 获取下载链接
        download_url = self.get_download_url(chrome_version)
        # 下载 ChromeDriver
        download_path = self.download_chromedriver(download_url)
        print(download_path)

        # 解压缩 ChromeDriver
        self.extract_chromedriver(download_path)
        # 清理下载的文件
        self.clean_up(download_path)

# 创建 ChromeDriverDownloader 类的实例
downloader = ChromeDriverDownloader()
# 执行下载并解压缩
downloader.download_chromedriver_for_current_browser()
