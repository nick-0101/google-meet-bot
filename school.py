import schedule
import time
import datetime
from datetime import date
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# Google Credentials
g_email = "nice try"
g_pass = "nice try"


def firstClass(g_email, g_pass):
    # Set browser to Global to prevent it from being garbage collected
    global browser

    # Initiate the browser
    options = Options()
    options.add_argument("window-size=1920,1080")
    # change to profile path
    options.add_argument('--profile-directory=Profile 1')
    options.add_argument('use-fake-ui-for-media-stream')

    browser = webdriver.Chrome(
        ChromeDriverManager().install(), options=options)

    # Open the Website
    browser.get('https://accounts.google.com/ServiceLogin?service=chromiumsync')

    # Focus Email
    browser.find_element_by_id('Email').click()

    # Log Into Google
    browser.find_element_by_name("Email").send_keys(g_email)
    browser.find_element_by_id('next').click()
    browser.find_element_by_name("Passwd").send_keys(g_pass)
    browser.find_element_by_id('submit').click()

    #  Wait for 3 seconds (for google to load)
    time.sleep(2.5)

    # Open new tab
    browser.get('https://classroom.google.com/u/2/hc')

    # Wait for 3 seconds (for classroom to load)
    time.sleep(3)

    # Open class (Geo)
    browser.get('https://classroom.google.com/u/2/c/MjI5MjYxMjEyNzY3')

    # Wait 3 seconds (for google meet to load)
    time.sleep(4)

    # Click Link
    browser.find_element_by_xpath(
        '//*[@id="yDmH0d"]/div[2]/div/div[1]/div/div[2]/div[2]/div/span/a').click()

    # Wait for 10 seconds
    time.sleep(10)

    # Click Join
    browser.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div[2]').click()

    # Re-resize browser window
    browser.set_window_size(1366, 784)


# ------------------------------------------ #

def secondClass(g_email, g_pass):
    # Set browser to Global to prevent it from being garbage collected
    global browser

    # Initiate the browser
    options = Options()
    options.add_argument("window-size=1920,1080")
    # change to profile path
    options.add_argument('--profile-directory=Profile 1')

    browser = webdriver.Chrome(
        ChromeDriverManager().install(), options=options)

    # Open the Website
    browser.get('https://accounts.google.com/ServiceLogin?service=chromiumsync')

    # Focus Email
    browser.find_element_by_id('Email').click()

    # Log Into Google
    browser.find_element_by_name("Email").send_keys(g_email)
    browser.find_element_by_id('next').click()
    browser.find_element_by_name("Passwd").send_keys(g_pass)
    browser.find_element_by_id('submit').click()

    #  Wait for 3 seconds (for google to load)
    time.sleep(2.5)

    # Open new tab
    browser.get('https://classroom.google.com/u/2/hc')

    # Wait for 3 seconds (for classroom to load)
    time.sleep(3)

    # Open class (Gym)
    browser.find_element_by_xpath(
        '//*[@id="yDmH0d"]/div[2]/div/div[2]/div/ol/li[2]/div[1]/div[3]/h2/a[1]').click()

    # Wait 3 seconds (for google meet to load)
    time.sleep(4)

    # Click Link
    browser.find_element_by_xpath(
        '//*[@id="yDmH0d"]/div[2]/div[2]/div[1]/div/div[2]/div[2]/div/span/a').click()

    # Mute mic and join
    browser.find_element_by_class_name('sUZ4id').click()

    # Wait for 3.5 seconds
    time.sleep(3.5)

    # Dismiss microphone alert
    browser.find_element_by_xpath(
        '//*[@id="yDmH0d"]/div[4]/div/div[2]/div[3]/div/span/span').click()

    # Click Join
    # browser.find_element_by_xpath(
    #     '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span').click()

    # Re-resize browser window
    browser.set_window_size(1366, 784)


# Get current date and time
date = datetime.datetime.today().weekday()
hour = datetime.datetime.now()

# School days
days = [0, 1, 2, 3, 4]

# First class
first_class_hour = 8
first_class_minute = 30
# Second class
second_class_hour = 12
second_class_minute = 30


# Start timer
start_time = time.time()

# print(hour.hour, first_class_hour, ':', hour.minute, first_class_minute)
if date in days and hour.hour == first_class_hour and hour.minute == first_class_minute:
    firstClass(g_email, g_pass)
elif date in days and hour.hour == second_class_hour and hour.minute == second_class_minute:
    secondClass(g_email, g_pass)
else:
    print('No class ツ')
    None

# Time to run
print("--- %s seconds ---" % (time.time() - start_time))
