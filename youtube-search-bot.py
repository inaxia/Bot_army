# This code will take a key that you want to search in Youtube. (LINE: 16-17)
# Run the code and it will open Youtube and search it for you.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# This will open Chrome browser
driver = webdriver.Chrome(ChromeDriverManager().install())

# This will open Youtube
driver.get('https://youtube.com')

# This will click on the search bar
searchBar = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
searchBar.click()

# Search for something
searchBar.send_keys('Python')

# This will click on search button
searchButton = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button')
searchButton.click()
