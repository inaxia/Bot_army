from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

email = 'email'
password = 'password'

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=6c27f393-19bc-4874-9eb5-c64a20896db8&client-request-id=393cb040-3ff7-432b-8339-63ab0a2dfdae&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=e46dd5e0-1cd0-4f25-95a5-3a44433675da&domain_hint=&sso_reload=true')

emailIdField = driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]')
emailIdField.click()

emailIdField.send_keys(email)

nextButton = driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div/input')
nextButton.click()

time.sleep(1)

passwordField = driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/input')
passwordField.click()

passwordField.send_keys(password)

signInButton = driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input')
signInButton.click()
