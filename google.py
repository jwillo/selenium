from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

url = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(chrome_options=chrome_options)

    # Navigate to url
driver.get("http://www.google.com")

    # Enter "webdriver" text and perform "ENTER" keyboard action
driver.find_element(By.NAME, "q").send_keys("webdriver" + Keys.ENTER)