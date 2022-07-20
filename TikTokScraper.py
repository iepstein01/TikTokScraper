from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
from selenium import webdriver
from fake_useragent import UserAgent, FakeUserAgentError
import os
import time
import json
import pickle

# Create Chrome Driver
service = Service(executable_path=ChromeDriverManager().install())
options = Options()
options.add_argument("start-maximized")

# Chrome is controlled by automated test software
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

# avoiding detection
options.add_argument("--disable-blink-features=AutomationControlled")

# Create webdriver
driver = webdriver.Chrome(options=options, service=service)

# Login
driver.get("https://www.tiktok.com")
with open("./TikTokCookies.json", "r") as cookiesfile:
    cookies = json.load(cookiesfile)
    for cookie in cookies:
        if "sameSite" in cookie:
            if cookie["sameSite"] == "None":
                cookie["sameSite"] = "Strict"
        print(cookie)
        driver.add_cookie(cookie)
time.sleep(10)
driver.quit()
