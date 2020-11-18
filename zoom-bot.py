# This code will take a few information from you like: (PROVIDE THESE DETAILS BEFORE RUNNING THE CODE)
# Your email, password, meet link, entry time and exit time. (LINE: 10-15)
# RUN THE CODE ANYTIME, it will automatically join and leave the class as per your entryTime and exitTime.

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
from datetime import datetime

# Enter some details
url = '743 1964 7505'
email = 'email'
password = 'passwordd'
entryTime = '15:10'
exitTime = '15:20'

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
        # driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://us04web.zoom.us/')

        # Sign in button
        clickButton('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div/ul[2]/li[5]/a', 0)

        # Sign in with google button
        clickButton('/html/body/div[1]/div[3]/div[2]/div[3]/div/div[3]/div/div[4]/a[2]', 5)

        # Email field
        clickAndType('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input', 0, email)

        # Next button
        clickButton('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]', 0)
        
        # Password field
        clickAndType('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input', 5, password)

        # Sign In button button
        clickButton('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]', 0)

        # Join a meeting button
        clickButton('/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div/ul[2]/li[1]/a', 20)

        # Url field
        clickAndType('/html/body/div[1]/div[3]/div[2]/div[3]/div/div[3]/form/div[1]/div/input', 5, url)

        # Join button
        clickButton('/html/body/div[1]/div[3]/div[2]/div[3]/div/div[3]/form/div[2]/div/a', 0)
        
        # Launch meeting button
        clickButton('/html/body/div[2]/div[2]/div/div[1]/div', 10)

        # Join from your browser button
        clickButton('/html/body/div[2]/div[2]/div/div[2]/h3[2]/a', 5)

        # To perform this task only once
        isJoined = True

    elif (datetime.now().strftime('%H:%M')) == exitTime:
        
        # Leave button
        clickButton('/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div/footer/div/div[3]/div/button', 0)

        # Leave meeting button
        clickButton('/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div/footer/div[2]/div[2]/div[3]/div/div/button', 0)

        # Ternimate the loop
        isClassCompleted = True

    else:
        time.sleep(5)
