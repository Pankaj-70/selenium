from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


brave_path = '/bin/brave-browser'
options = Options()
options.binary_location = brave_path
driver = webdriver.Chrome(options = options)


driver.get('https://quotes.toscrape.com/')
quotes = driver.find_elements(By.XPATH, "//span[@class='text']")
authors = driver.find_elements(By.CSS_SELECTOR, "small[class='author']")

# for quote in quotes:
#     print(quote.text)
# for author in authors:
    # print(author.text)

for quote, author in zip(quotes, authors):
    print(f"{quote.text} - {author.text}")




driver.quit()
