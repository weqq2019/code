from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By



# 指定 chromedriver.exe 文件的路径
service =ChromeService(executable_path=r"D:\BaiduSyncdisk\LQ\Code\M17\Code\03_utilities\chromedriver_win32\chromedriver.exe")

# 创建 Chrome 浏览器实例
options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
# driver = webdriver.Chrome(driver_path, options=options)
driver = webdriver.Chrome(service=service, options=options)



# 打开网页
driver.get("https://www.google.com")

# 在搜索框中输入关键字
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Python")
search_box.send_keys(Keys.RETURN)

# 等待搜索结果加载完成
driver.implicitly_wait(10)

# 获取搜索结果
results = driver.find_elements(By.CSS_SELECTOR, "div.g")

# 输出搜索结果标题和链接
for result in results:
    # print(result.find_element_by_css_selector("h3").text)
    # print(result.find_element_by_css_selector("a").get_attribute("href"))
    
    # 使用 find_element_by_css_selector 方法获取 h3 和 a 标筴�，如案件中，h3 标筴�包含了标题，a 标筴�包含了银接地�n，将其分别返回给 title 和 link 变量。
    # 最后，进行打印调试。
    
    title_element = result.find_element(By.CSS_SELECTOR, "h3")
    # title = result.find_element_by_css_selector("h3").text
    link_element = result.find_element(By.CSS_SELECTOR, "a")
    link=link_element.get_attribute("href")

    print(title_element, link)

   

# 关闭浏览器
driver.quit()
    