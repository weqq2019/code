from unicodedata import name
import winreg
import requests
import json
import re
import zipfile
import os

# 解压zip文件
def un_zip(file_name):
    zip_file = zipfile.ZipFile(file_name)
    if os.path.isdir(file_name + "/把此文件夹下驱动程序放到“右击桌面谷歌浏览器快捷键打开文件所在位置”的文件夹内容"):
        pass
    else:
        os.mkdir(file_name + "/把此文件夹下驱动程序放到“右击桌面谷歌浏览器快捷键打开文件所在位置”的文件夹内容")
    for names in zip_file.namelist():
        zip_file.extract(names, file_name + "/把此文件夹下驱动程序放到“右击桌面谷歌浏览器快捷键打开文件所在位置”的文件夹内容/")
    zip_file.close()

# 获取本地Chrome浏览器版本
FullChromeVersion = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\Google Chrome'), 'DisplayVersion')[0]
ChromeVersion = int(FullChromeVersion.split('.')[0])
print('Chrome version: ' + FullChromeVersion)

# 获取可用的Chrome驱动版本列表
url = "https://registry.npmmirror.com/-/binary/chromedriver/"
header_guishudi = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}
response = requests.get(url, headers=header_guishudi, verify=True)
content = response.content.decode('utf8')
contents = json.loads(content)


names = []
for i in contents:

    name = i['name']
    a = re.match('1', name)
    try:
        aa = a.group()
        if aa == '1':
            names.append(name)
    except:
        continue
# print(str(names))

# 下载并安装相应版本的Chrome驱动
if str(FullChromeVersion) in str(names):
    print(FullChromeVersion)
    print('在里面')
    banben = FullChromeVersion
    url = "https://cdn.npmmirror.com/binaries/chromedriver/{}/chromedriver_win32.zip".format(banben)
    header_guishudi = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }
    response = requests.get(url, headers=header_guishudi).content
    file_name = "{}.zip".format(banben)
    file_name = str(file_name).replace("/", '')
    with open(file_name, 'wb') as f:
        f.write(response)
else:
    print('不在里面')
    for n in names:
        if str(ChromeVersion) in n:
            print(n)
            banben = n
