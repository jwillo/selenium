# Pything Selenium Script

To get this going, you need to 
 - install python for windows (This was usig Version 3.11)
 - install the auto_py_to_exe so you can run it anywhere. https://pypi.org/project/auto-py-to-exe/ (I used the pip method); `pip install auto-py-to-exe'
 - install the python selenium modules, (Again using pip); `pip install selenium`
 - Download and install the webdriver from https://chromedriver.chromium.org/home (make sure it is the same version as the installed version of chrome, I am using version 109.
 - Once the script work as a script, I complied it using the auto_py_to_exe 
 
 # What this Script does.
 
 This script launches the URL (Passed as the 3rd paramater if needed, or can be hardcoded as I have), and then find the username and password fields, and fills them with the username and password as passed from the 1st and 2nd paramaters.
 
 The Use case in this scenario was for Airflow control Panel inside and AWS instance.
 
 I am launching this from inside a session connector, I am also using chrome flags to lock / down secure it even more, including..
 
 - Icognito window (so it does not save session information or other cookies once the browser is closed)
 - App mode ( there is no URL bar, so the end user cannot type in another URL on the network
 - Disable the chrome in build password saving tool, so password cant be saved in the browser.
 
 
 
