from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

import time

options = Options()
options.add_argument("--disable-notifications")

chrome = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
chrome.get("https://www.facebook.com/")

email = chrome.find_element_by_id("email")
password = chrome.find_element_by_id("pass")

email.send_keys('fain73@hotmail.com')
password.send_keys('a0963798289')
password.submit()

time.sleep(3)
chrome.get('https://www.facebook.com/learncodewithmike')

# 利用Selenium套件的execute_script()方法 執行滾動捲軸的JavaScript程式碼
for x in range(1, 4):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)

soup = BeautifulSoup(chrome.page_source, 'html.parser')

titles = soup.find_all('span', {
    'class': 'a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7'})

for title in titles:
    print(title.getText())

for img in soup.find_all(class_="_5dec"):
    print(img.get("src"))

chrome.quit()