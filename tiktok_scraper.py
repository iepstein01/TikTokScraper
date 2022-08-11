from tiktok_login import login
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


def create_chrome_driver():
    # Create Chrome Driver
    service = Service(executable_path=ChromeDriverManager().install())
    options = Options()

    # Chrome is controlled by automated test software
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)

    # avoiding detection
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Person 1
    options.add_argument("--profile-directory=Default")

    # Person 2
    # options.add_argument("--profile-directory=Profile 1")

    # Path to User Data directory
    options.add_argument(
        "--user-data-dir=/Users/itaiepstein/Library/Application Support/Google/Chrome"
    )

    # Create webdriver
    driver = webdriver.Chrome(options=options, service=service)
    return driver


# TODO: start by clicking on the first video or maybe scroll down between the first few
# TODO: just have it interact with the video, click through them, like some of the videos, watch it for a certain amount of time based on a standard normal distribution
# TODO: how likely is it that they watch a video not tagged relevant to their interests?

"""# Pause all videos on the website to ensure bot can access watch them in full
    driver.execute_script(
        'videos = document.querySelectorAll("video"); for(video of videos) {video.pause()}'
    )"""
