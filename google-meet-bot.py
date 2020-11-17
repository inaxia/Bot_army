# This code will take a few information from you like: (PROVIDE THESE DETAILS BEFORE RUNNING THE CODE)
# Your email, password, meet link, entry time and exit time. (LINE: 10-15)
# RUN THE CODE ANYTIME, it will automatically join and leave the class as per your entryTime and exitTime.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime

# Enter some details
url = 'abc-defg-hij'
email = 'email'
password = 'password'
entryTime = '19:10'
exitTime = '19:12'

isJoined = False
isClassCompleted = False

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
while not isClassCompleted:
    if ( (datetime.now().strftime('%H:%M')) == entryTime ) and ( isJoined == False ):

        # This will open Chrome browser
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&&o_ref=https%3A%2F%2Fwww.google.com%2F&_ga=2.10346736.430892883.1605431766-1750922843.1605431766&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

        # Email field
        clickAndType('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input', 0, email)

        # Next button
        clickButton('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]', 0)
        
        # Password field
        clickAndType('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input', 3, password)

        # Sign In button button
        clickButton('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]', 0)

        # Join or start a meeting button
        clickButton('/html/body/div[1]/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div[1]/div/div/div[1]', 10)

        # Code entry field
        clickAndType('/html/body/div[1]/div[3]/div/div[2]/span/div/div[2]/div[1]/div[1]/input', 0, url)

        # Continue button
        clickButton('/html/body/div[1]/div[3]/div/div[2]/span/div/div[4]/div[2]/div/span', 3)

        # Dismiss button
        clickButton('/html/body/div/div[3]/div/div[2]/div[3]/div/span/span', 10)

        # Ask to join button
        clickButton('/html/body/div/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span', 5)

        # To perform this task only once
        isJoined = True

    elif (datetime.now().strftime('%H:%M')) == exitTime:
        
        # Leave button
        clickButton('/html/body/div[1]/c-wiz/div[1]/div/div[8]/div[3]/div[9]/div[2]/div[2]/div', 0)

        # Ternimate the loop
        isClassCompleted = True

    else:
        time.sleep(5)
