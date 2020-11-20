# This code will take a few information from you like: (PROVIDE THESE DETAILS BEFORE RUNNING THE CODE)
# Your email and password. (LINE: 9-11)
# Read 'the last line'.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

# Enter some details
email = 'email'
password = 'password'

# To click a button
def clickButton(position, sleepTime):
    time.sleep(sleepTime)
    driver.find_element_by_xpath(position).click()

# To type something
def clickAndType(position, sleepTime, word):
    time.sleep(sleepTime)
    field = driver.find_element_by_xpath(position)
    field.click()
    field.send_keys(word)


# Main code
# This will open Chrome browser
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=6c27f393-19bc-4874-9eb5-c64a20896db8&client-request-id=393cb040-3ff7-432b-8339-63ab0a2dfdae&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=e46dd5e0-1cd0-4f25-95a5-3a44433675da&domain_hint=&sso_reload=true')

# Email field
clickAndType('/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]', 0, email)

# Next button
clickButton('/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div/input', 5)

# Password field
clickAndType('/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]/div/div[2]/input', 3, password)

# Sign in button
clickButton('/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div/div/input', 0)

# Don't show again checkbox
clickButton('/html/body/div/form/div[1]/div/div[1]/div[2]/div/div[2]/div/div[3]/div[1]/div/label/input', 0)

# Yes button
clickButton('/html/body/div/form/div[1]/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input', 0)

# Use the web app button
clickButton('/html/body/promote-desktop/div/div/div/div[1]/div[2]/div/a', 5)

# Calender button
# clickButton('/html/body/div[1]/div[2]/div[1]/app-bar/nav/ul/li[5]/button', 5)

# # Calender join utton
# clickButton('/html/body/div[1]/div[2]/div[2]/div[1]/div/div/calendar-bridge/div/div[4]/div[2]/div/div/div[1]/div/div[3]/div[2]/div[3]/div[2]/div/div[2]/button', 5)

# # Mic off button
# clickButton('/html/body/div[1]/div[2]/div[2]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[2]/div/button/span[1]', 5)

# # Camera off button
# clickButton('/html/body/div[1]/div[2]/div[2]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]', 5)

# # Join button
# clickButton('/html/body/div[1]/div[2]/div[2]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button', 5)

# the last line:
# MICROSOFT TEAMS DOES'T ALLOW WEB AUTOMATION. THIS BOT WILL JUST STOP WORKING AS SOON AS IT WILL ENTER THE TEAMS.
