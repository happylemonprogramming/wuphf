# Need to make private!
email = 'claytonlemons@live.com'
password = '21$Milkshake'

prompt = 'Is it gif or gif?'
path = r"C:\Users\clayt\Documents\Programming\banana.gif"

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def instagram_post(prompt,path):
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
    wd.get("https://www.instagram.com/")
    # Log in
    wd.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(email)
    wd.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
    wd.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button').click()
    time.sleep(4)
    # # Maybe add if statement for if notifications or log in info are present?
    # Save Login Info Pop-Up
    # /html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div/div/button #old0
    wd.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button').click()
    # Notifications Pop-Up
    wd.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
    # Post
    # /html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/div/a/div
    wd.find_element_by_xpath('/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div[3]/div/button').click()
    time.sleep(3)
    # Post Image
    wd.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/form/input').send_keys(path)
    # # Add if statement if video to close Reels notification
    # Reels Notification
    wd.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div/div[4]/button').click()
    # Hit Next
    wd.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button').click()
    # (Eventually Add Filters)
    # Hit Next Again
    wd.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button').click()
    # Add Text Caption
    wd.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/textarea').send_keys(prompt)
    time.sleep(5)
    # Share
    wd.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/button').click()
    time.sleep(30)

instagram_post(prompt,path)