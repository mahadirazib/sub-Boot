import csv
import os
import time
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller


youtubeLink = input("Please enter your Channel link: \n")


f =  open("ID and Pass.csv" , "r")

idAndPass = csv.reader(f)

for line in idAndPass:
    if (len(line)==2):

        driver = uc.Chrome(use_subprocess=True)

        email = line[0]
        password = line[1]


        wait = WebDriverWait(driver, 20)
        url = 'https://accounts.google.com/ServiceLogin?service=accountsettings&continue=https://myaccount.google.com%3Futm_source%3Daccount-marketing-page%26utm_medium%3Dgo-to-account-button'
        driver.get(url)

        driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]')
        
        keyboard = Controller()

        keyboard.type(email)

        print(email)

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        time.sleep(3)

        try:
            driver.find_element(by=By.XPATH, value='//*[@id="password"]/div[1]/div/div[1]/input')

            keyboard.type(password)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)


            if (driver.find_element(by=By.XPATH, value='//div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[2]').text == 'Wrong password. Try again or click Forgot password to reset it.'):
        
                print('This email: <--- '+email+' ---> is corrct but pass is wrong.')

                driver.close()
                continue

            else:

                time.sleep(3)

                driver.get(youtubeLink)

                subButton = driver.find_element_by_id("subscribe-button")
                
                if (subButton.text == "SUBSCRIBE"):
                    subButton.click()
                    print("Not ", subButton.text+"D")


        except:
            driver.close()
            continue

        driver.close()       


    else:
        print("Id: <--- " + line[0] + " --->Has no Password.")

    

f.close