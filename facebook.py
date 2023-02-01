# need to make private!
secret = 'f7cabaab119d7bd8dcafb3bec28c5cc3'
app_id = '554211022979973'
access_token = '554211022979973|SWyobgqnf8wkaK7CW4kbeKQGaHc'
email = 'doesitwork@onmail.com'
password = '21$Milkshake'

# prompt = 'yo yo yo yo'
# path = r"C:\Users\clayt\Pictures\AI Images\Lemon & T-Rex.png"

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def facebook_post(prompt,path):
    # Find Brave browser path (works with any Chromium browser) and go incognito mode
    driver_path = r"C:\Users\clayt\Documents\Programming\chromedriver.exe"
    # brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument("--incognito")
    # options.binary_location = brave_path
    options.binary_location = chrome_path

    # Open website
    wd = webdriver.Chrome(executable_path=driver_path, options=options)
    wd.implicitly_wait(100)
    wd.maximize_window()
    wd.get("https://www.facebook.com/")
    # Log in
    wd.find_element_by_xpath('//*[@id="email"]').send_keys(email)
    wd.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
    wd.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
    time.sleep(4)

    # Profile Page
    wd.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div/a/div[1]/div[2]/div/div/div/div/span/span').click()
    time.sleep(3)
    # Post Text
    wd.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[2]/div[1]/div/div/div[4]/div[2]/div/div[2]/div[1]/div/div/div/div/div[1]/div/div[1]/span').click()
    wd.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]/p').send_keys(prompt)
    # Post Image
    wd.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[1]/div[2]/div/div[1]/div/span/div/div/div[1]/div/div/div[1]/i').click()
    wd.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[2]/div/div[1]/div/div/input').send_keys(path)
    # Publish
    time.sleep(4)
    wd.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div').click()
