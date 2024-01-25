from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# 无界面模式 真正开发中不需要打开浏览器界面，后台运行即可
options.add_argument("--headless")

driver = webdriver.Chrom(options=options)

url = 'https://www.jd.com/'
driver.get(url)

content = driver.page_source
print(content)
