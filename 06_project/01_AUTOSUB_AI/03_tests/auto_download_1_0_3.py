import requests
from zipfile import ZipFile
import os
import winreg

class ChromeDriverDownloader:
    # 在初始化方法中，将下载目录作为参数传入
    def __init__(self, directory_to_download):
        self.directory_to_download = directory_to_download

    # 此方法用于获取浏览器的版本
    def get_version_of_browser(self):
        version_of_browser = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                                             'SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome'),
                                              'DisplayVersion')[0]
        return version_of_browser

    # 此方法用于从浏览器版本中提取 Chrome 版本
    def get_version_of_chrome(self, version_of_browser):
        parts_of_version = version_of_browser.split('.')
        parts_of_version.pop()  # 删除最后一部分
        version_of_chrome = '.'.join(parts_of_version)
        return version_of_chrome

    # 此方法用于根据 Chrome 版本获取下载链接
    def get_url_for_download(self, version_of_chrome):
        url_of_release = f'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{version_of_chrome}'
        response_from_request = requests.get(url_of_release)
        version_of_latest = response_from_request.text.strip()
        url_for_download = f'https://chromedriver.storage.googleapis.com/{version_of_latest}/chromedriver_win32.zip'
        return url_for_download

    # 此方法用于下载 ChromeDriver 并将其保存到预定的目录
    def download_chromedriver(self, url_for_download):
        file_for_download = 'chromedriver_win32.zip'
        path_for_download = os.path.join(self.directory_to_download, file_for_download)

        response_from_request = requests.get(url_for_download)
        with open(path_for_download, 'wb') as file_obj:
            file_obj.write(response_from_request.content)

        return path_for_download

    # 此方法用于解压缩已下载的 ChromeDriver
    def extract_chromedriver(self, path_for_download):
        with ZipFile(path_for_download, 'r') as zip_file_obj:
            zip_file_obj.extractall(self.directory_to_download)

    # 此方法用于清理已下载的 zip 文件
    def clean_up_downloaded_file(self, path_for_download):
        os.remove(path_for_download)

    # 此方法整合了上述所有步骤，用于为当前的浏览器版本下载和解压缩 ChromeDriver
    def download_chromedriver_for_current_browser(self):
        version_of_browser = self.get_version_of_browser()
        version_of_chrome = self.get_version_of_chrome(version_of_browser)
        url_for_download = self.get_url_for_download(version_of_chrome)
        path_for_download = self.download_chromedriver(url_for_download)
        self.extract_chromedriver(path_for_download)
        self.clean_up_downloaded_file(path_for_download)

# 创建 ChromeDriverDownloader 类的实例，并指定下载目录
downloader_instance = ChromeDriverDownloader('06_project/01_AUTOSUB_AI/03_tests/download')
# 调用 download_chromedriver_for_current_browser 方法，开始下载和解压缩操作
downloader_instance.download_chromedriver_for_current_browser()
