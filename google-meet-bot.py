from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from datetime import datetime

url = 'abc-defg-hij'
email = 'email'
password = 'password'

isJoined = False
isClassCompleted = False

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&&o_ref=https%3A%2F%2Fwww.google.com%2F&_ga=2.10346736.430892883.1605431766-1750922843.1605431766&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

def clickButton(xpath, sleepTime):
    time.sleep(sleepTime)
    driver.find_element_by_xpath(xpath).click()

while not isClassCompleted:
    if (datetime.now().strftime('%H:%M') == '12:19') and (isJoined == False):

        emailField = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
        emailField.click()
        emailField.send_keys(email)

        nextButton = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
        nextButton.click()

        time.sleep(3)

        passwordField = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
        passwordField.click()
        passwordField.send_keys(password)

        signInButton = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]')
        signInButton.click()

        time.sleep(5)

        joinButton = driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div/div/div/div[2]/div[2]/div[2]/div/c-wiz/div[1]/div/div/div[1]')
        joinButton.click()

        codeInput = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/span/div/div[2]/div[1]/div[1]/input')
        codeInput.click()
        codeInput.send_keys(url)

        time.sleep(3)

        continueButton = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/span/div/div[4]/div[2]/div/span')
        continueButton.click()

        time.sleep(5)

        dismissAll = driver.find_element_by_xpath('/html/body/div/div[3]/div/div[2]/div[3]/div/span/span')
        dismissAll.click()

        time.sleep(3)

        askToJoin = driver.find_element_by_xpath('/html/body/div/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span')
        askToJoin.click()

        isJoined = True

    else:
        time.sleep(5)
        print('...', end='|')
