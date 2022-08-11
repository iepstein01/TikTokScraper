from tiktok_scraper import create_chrome_driver
from tiktok_login import login
from tiktok_video_interactions import like_video, next_video

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


def relevant_tags(driver):
    # wait until comment section is loaded
    WebDriverWait(driver, timeout=60).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[2]/div[2]/div[1]')
        )
    )

    comment_parent_element = driver.find_element(
        By.XPATH, '//*[@id="app"]/div[2]/div[3]/div[2]/div[2]/div[1]'
    )
    comment_parent_children = comment_parent_element.find_elements(By.TAG_NAME, "a")
    comment_categories = [
        child.get_attribute("href") for child in comment_parent_children
    ]
    tags = []
    for category in comment_categories:
        if "tag" in category:
            tag = category.split("/")[-1]
            tags.append(tag)

    return tags
