from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

brave_path = '/bin/brave-browser'

options = Options()
options.binary_location = brave_path

# 👇 Run in background (headless mode)
options.add_argument("--headless=new")  

driver = webdriver.Chrome(options=options)

driver.get('https://en.wikipedia.org/wiki/Arun_Khetarpal')

links = driver.find_elements(By.TAG_NAME, "a")
for i, link in enumerate(links):
    if i == 11:
        break
    print(link.text, link.get_attribute("href"))

driver.quit()