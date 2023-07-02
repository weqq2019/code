import requests
dd=requests.get('http://www.baidu.com').text.strip()

print(dd)


