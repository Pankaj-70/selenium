from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#configuring browser
options = Options()
options.binary_location = "/usr/bin/google-chrome"
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

#start browser
driver = webdriver.Chrome(options=options)

#open website
driver.get('https://google.com')

#extract data
print('Title', driver.title)
print('URL:', driver.current_url)

#close browser
driver.quit()