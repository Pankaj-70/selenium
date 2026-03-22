from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


brave_path = '/bin/brave-browser'
options = Options()
options.binary_location=brave_path

driver = webdriver.Chrome(options=options)

driver.get('https://google.com')


search = driver.find_element(By.CSS_SELECTOR, "textarea[name='q']")
search.send_keys('selenium python')
search.clear()
search.send_keys('rms chail')
search.submit()

driver.quit()

