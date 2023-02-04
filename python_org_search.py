import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


url = "http://192.168.102.107:8080"
#$username = sys.argv[1]
#$password = sys.argv[2]

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument ('--incognito')
chrome_options.add_argument ("--app=" + url)
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-save-password-bubble")
driver = webdriver.Chrome(chrome_options=chrome_options)


username = driver.find_element(By.ID,"username")
password = driver.find_element(By.ID,"password")

username.send_keys("airflow")
password.send_keys("airflow")
password.send_keys(Keys.RETURN)
