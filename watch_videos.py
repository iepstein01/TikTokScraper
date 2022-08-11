from tiktok_scraper import create_chrome_driver
from tiktok_login import login
from tiktok_video_interactions import like_video, next_video
from relevant_tags import relevant_tags
from user_interests import get_interests

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
from selenium import webdriver
from fake_useragent import UserAgent, FakeUserAgentError
import numpy as np
import time

driver = create_chrome_driver()
interests = get_interests()
f = open("video_recommendations.txt", "x")
driver.get("https://www.tiktok.com")
# login(driver)

# Click on first post to enter mobile like viewing state
WebDriverWait(driver=driver, timeout=60).until(
    EC.element_to_be_clickable(
        (
            By.XPATH,
            '//*[@id="app"]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[1]',
        )
    )
).click()

def watch_n_minutes(low, high)
    return np.random.randint(low=low, high=high)

def watch_n_videos(driver, n):
    for i in range(n):
        if watch_or_skip(driver, interests, tags)
        time.sleep(5)
        next_video(driver)

def get_video_length(driver):
    video_length = str(
            WebDriverWait(driver=driver, timeout=60)
            .until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//*[@id="app"]/div[2]/div[3]/div[1]/div[2]/div[2]/div[2]',
                    )
                )
            )
            .get_attribute("innerHTML")
        )
    video_length = video_length[video_length.index("/") + 1 : len(video_length)]
    if video_length[0:1] == "0":
        video_length = video_length[1 : len(video_length)]
    video_minutes = video_length[0 : video_length.index(":")]
    video_seconds = video_length[video_length.index(":") + 1 : len(video_length)]
    video_length_in_seconds = int(video_minutes) * 60 + int(video_seconds)
    return video_length_in_seconds

def watch_or_skip(driver, interests, tags):
    is_of_interest = False
    for interest in interests:
        for tag in tags:
            if interest.lower() == tag.lower():
                is_of_interest = True
                break
        if is_of_interest:
            return is_of_interest

def collect_video_info(driver):
    current_vid = driver.current_url
    tags = relevant_tags



# Watch 5 videos
watch_n_videos(driver, 5)


driver.quit()