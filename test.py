from tiktok_scraper import create_chrome_driver
from tiktok_login import login
from tiktok_video_interactions import like_video, next_video
from relevant_tags import relevant_tags

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
from selenium import webdriver
from fake_useragent import UserAgent, FakeUserAgentError
import numpy
import time

driver = create_chrome_driver()
driver.get("https://www.tiktok.com")
time.sleep(2)
WebDriverWait(driver=driver, timeout=60).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="app"]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[1]',
        )
    )
).click()
tags = relevant_tags(driver)
