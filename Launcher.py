import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

username = sys.argv[1]
password = sys.argv[2]

##uncomment the second line, and comment out the first to allow URL input from the input arguments.

url = "http://192.168.102.107:8080"
#url = sys.argv[3] 

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument ('--incognito')
chrome_options.add_argument ("--app=" + url)
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-save-password-bubble")
driver = webdriver.Chrome(chrome_options=chrome_options)


username_input = browser.find_element_by_id("username")
username_input.send_keys(username)

password_input = browser.find_element_by_id("password")
password_input.send_keys(password)

# Submit the form
password_input.send_keys(Keys.RETURN)