import re
import requests
from zipfile import ZipFile
import os
import winreg
import subprocess


class Browser:
    def __init__(self):
        """
        初始化浏览器类并创建下载文件夹。
        """
        self.download_dir = self.create_download_folder()

    def get_browser_version(self):
        """
        获取本地浏览器版本。

        Returns:
            str: 本地浏览器的版本号。

        Notes:
            此方法仅适用于 Windows 操作系统和 Google Chrome 浏览器。
        """
        # 获取本地浏览器版本
        browser_version = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                                                             'SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome'),
                                              'DisplayVersion')[0]
        return browser_version

    def get_chrome_version(self, browser_version):
        """
        从浏览器版本中提取 Chrome 版本。

        Args:
            browser_version (str): 浏览器版本号。

        Returns:
            str: Chrome 版本号。

        Notes:
            此方法假设浏览器版本号遵循标准的 x.y.z 格式。
            例如，如果浏览器版本为 "94.0.4606.81"，则提取的 Chrome 版本为 "94.0.4606"。
        """
        # 分割浏览器版本号并删除最后一部分
        version_parts = browser_version.split('.')
        version_parts.pop()
        chrome_version = '.'.join(version_parts)
        return chrome_version

    def get_latest_version_and_download_url(self, chrome_version):
        """
        根据 Chrome 版本获取最新版本的驱动程序版本号和下载链接。

        Args:
            chrome_version (str): Chrome 版本号。

        Returns:
            tuple: 包含最新版本的驱动程序版本号和对应的下载链接。

        Notes:
            此方法使用 ChromeDriver 的下载链接模板，并将 Chrome 版本号插入其中。
            例如，如果 Chrome 版本为 "94.0.4606"，则生成的下载链接为 "https://chromedriver.storage.googleapis.com/94.0.4606/chromedriver_win32.zip"。
        """
        # 获取最新版本的下载链接
        release_url = f'https://chromedriver.storage.googleapis.com/LATEST_RELEASE_{chrome_version}'
        response = requests.get(release_url)
        latest_version = response.text.strip()
        download_url = f'https://chromedriver.storage.googleapis.com/{latest_version}/chromedriver_win32.zip'
        return latest_version, download_url

    def get_chromedriver_version(self):
        """
        获取本地安装的 Chromedriver 版本号。

        Returns:
            str or None: Chromedriver 版本号，如果未找到版本号则返回 None。
        """
        chromedriver_path = os.path.join(self.download_dir, "chromedriver.exe")
        # 检查 chromedriver 文件是否存在
        if not os.path.exists(chromedriver_path):
            return None
        
        result = subprocess.run([chromedriver_path, "--version"], capture_output=True, text=True)
        version = result.stdout.strip()
        pattern = r'ChromeDriver (\d+\.\d+\.\d+\.\d+)'
        match = re.search(pattern, version)
        if match:
            version_number = match.group(1)
            return version_number
        else:
            return None

    def check_chromedriver_exists(self):
        """
        检查 Chromedriver 是否存在于下载文件夹中。

        Returns:
            bool: 如果 Chromedriver 存在，则返回 True；否则返回 False。
        """
        chromedriver_path = os.path.join(self.download_dir, "chromedriver.exe")
        return os.path.exists(chromedriver_path)

    def create_download_folder(self):
        """
        在当前工作路径下创建下载文件夹路径。

        Returns:
            str: 下载文件夹的路径。

        Examples:
            >>> downloader = Browser()
            >>> download_folder = downloader.create_download_folder()
            >>> print(download_folder)
            /path/to/current_directory/download

        Notes:
            如果 "download" 文件夹已经存在，则不进行任何操作。
        """
        # 获取当前工作目录
        current_path = os.path.abspath(os.path.dirname(__file__))
        # 创建 "download" 文件夹路径
        download_path = os.path.join(current_path, "download")

        # 如果 "download" 文件夹不存在，则创建它
        if not os.path.exists(download_path):
            os.makedirs(download_path)
        return download_path

    def download_Browser(self, download_url):
        """
        下载 Browser 驱动程序。

        Args:
            download_url (str): 下载链接。

        Returns:
            str: 下载的文件路径。

        Notes:
            此方法使用 requests 库下载文件，并将其保存到指定路径。
        """
        # 下载 Browser
        download_file = 'chromedriver_win32.zip'
        download_path = os.path.join(self.download_dir, download_file)

        response = requests.get(download_url)
        with open(download_path, 'wb') as file:
            file.write(response.content)

        return download_path

    def extract_Browser(self, download_path):
        """
        解压缩 Browser 驱动程序。

        Args:
            download_path (str): 下载的文件路径。

        Notes:
            此方法使用 zipfile 库解压缩下载的文件，并将文件提取到下载文件夹中。
        """
        # 解压缩下载的文件
        with ZipFile(download_path, 'r') as zip_file:
            zip_file.extractall(self.download_dir)

    def clean_up(self, download_path):
        """
        清理下载的文件。

        Args:
            download_path (str): 下载的文件路径。

        Notes:
            此方法删除下载的文件，以清理不再需要的文件。
        """
        # 清理下载的文件
        os.remove(download_path)

    def download_Browser_for_current_browser(self):
        """
        根据本地浏览器版本下载相应版本的 Browser 驱动程序。
        """
        # 检查 Chromedriver 是否存在
        if not self.check_chromedriver_exists():
            # 如果不存在，创建下载文件夹
            self.create_download_folder()
        else:
            print("Chromedriver 已存在，无需下载。")
            return

        # 获取浏览器版本
        browser_version = self.get_browser_version()
        # 获取 Chrome 版本
        chrome_version = self.get_chrome_version(browser_version)

        # 获取最新版本和下载链接
        latest_version, download_url = self.get_latest_version_and_download_url(chrome_version)

        # 检查本地的 Chromedriver 版本
        local_version = self.get_chromedriver_version()

        # 如果本地版本和最新版本不匹配，下载并解压最新版本
        if local_version != latest_version:
            # 下载 Browser
            download_path = self.download_Browser(download_url)
            # 解压缩 Browser
            self.extract_Browser(download_path)
            # 清理下载的文件
            self.clean_up(download_path)


# 创建 Browser 类的实例
downloader = Browser()
# 执行下载并解压缩
downloader.download_Browser_for_current_browser()
