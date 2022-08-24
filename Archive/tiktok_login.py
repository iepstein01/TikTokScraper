from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
from selenium import webdriver
from fake_useragent import UserAgent, FakeUserAgentError
import time


def login(driver) -> bool:
    login_successful = False

    WebDriverWait(driver=driver, timeout=60).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/button')
        )
    ).click()
    time.sleep(2)
    WebDriverWait(driver=driver, timeout=60).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="loginContainer"]/div/div/a[2]'))
    ).click()
    time.sleep(2)
    WebDriverWait(driver=driver, timeout=60).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="loginContainer"]/div/form/div[2]/a')
        )
    ).click()
    time.sleep(2)
    WebDriverWait(driver=driver, timeout=60).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="loginContainer"]/div/form/div[1]/input')
        )
    ).send_keys("")
    time.sleep(2)
    WebDriverWait(driver=driver, timeout=60).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="loginContainer"]/div/form/div[2]/div/input')
        )
    ).send_keys("")
    time.sleep(2)
    WebDriverWait(driver=driver, timeout=60).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="loginContainer"]/div/form/button')
        )
    ).click()

    # Ensure CAPTCHA is completed (find better way to do this)
    response = str(input("Is the captcha completed? [Y/N]\n"))
    while True:
        if response.upper()[0:1] == "Y":
            print("login successful")
            login_successful = True
            break
        elif response.upper()[0:1] == "N":
            print("please fill in the captcha")

    return login_successful
