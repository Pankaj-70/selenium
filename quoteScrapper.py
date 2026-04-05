from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


brave_path = '/bin/brave-browser'
options = Options()
options.binary_location = brave_path
driver = webdriver.Chrome(options = options)
driver.implicitly_wait(10)


print('--------------------Logging In-------------------')
#login
driver.get('https://quotes.toscrape.com/login')
username = driver.find_element(By.CSS_SELECTOR, "input[id='username']")
password = driver.find_element(By.CSS_SELECTOR, "input[id='password']")
login = driver.find_element(By.XPATH, "//input[@value='Login']")
password.clear()
username.send_keys('pankaj3970')
username.clear()
username.send_keys('pankaj70')
password.send_keys('12345')
login.click()
print('--------------------Logged In-------------------')



print('--------------------Extracting quotes & authors-------------------')
driver.get('https://quotes.toscrape.com/')
quotes = driver.find_elements(By.XPATH, "//span[@class='text']")
authors = driver.find_elements(By.CSS_SELECTOR, "small[class='author']")

# for quote in quotes:
#     print(quote.text)
# for author in authors:
    # print(author.text)

for quote, author in zip(quotes, authors):
    print(f"{quote.text} - {author.text}")



print('--------------------Process finished-------------------')
driver.quit()
