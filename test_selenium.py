from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

sites = ['https://www.youtube.com/','https://net52.cc/home', 'https://google.com', 'https://github.com']
driver_path = '/home/pankaj/Downloads/chrome-linux64/chrome'
brave_path = '/bin/brave-browser'
#configuring browser
options = Options()
options.binary_location = brave_path

#start browser
# service = Service(driver_path)
driver = webdriver.Chrome(options=options)

#open website

'''
for site in sites:
    driver.get(site)

    #extract data
    print('Title', driver.title)
    print('URL:', driver.current_url)

'''

#search by input in google
# driver.get(sites[0])
# search = driver.find_element(By.NAME, "q")
# search.send_keys('rashtriya military school, chail')
# search.submit()

# #click on captcha button
# button = driver.find_element(By.XPATH, "//div[@class = 'recaptcha-checkbox-border']")


#search by input in youtube
# driver.get('https://youtube.com')
# search = driver.find_element(By.NAME, "search_query")
# search.send_keys('arijit singh latest songs')
# search.submit()





#close browser
driver.quit()