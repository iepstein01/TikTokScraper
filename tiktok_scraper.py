from Archive.tiktok_login import login
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

# TODO: start by clicking on the first video or maybe scroll down between the first few
# TODO: just have it interact with the video, click through them, like some of the videos, watch it for a certain amount of time based on a standard normal distribution
# TODO: how likely is it that they watch a video not tagged relevant to their interests?


class TikTok_Scraper:
    def __init__(self) -> None:
        # TODO: deal with this later
        self.user_data_dir = ""
        self.profile_dir = ""

    def create_chrome_driver(self):
        # Create Chrome Driver
        service = Service(executable_path=ChromeDriverManager().install())
        options = Options()

        # Chrome is controlled by automated test software
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        # avoiding detection
        options.add_argument("--disable-blink-features=AutomationControlled")

        # Add data directory path here
        # Path to User Data directory
        options.add_argument(
            "--user-data-dir=/Users/itaiepstein/Library/Application Support/Google/Chrome"
        )

        # Add already logged in Chrome Profile names here
        # Person 1
        options.add_argument("--profile-directory=Default")

        # Person 2
        # options.add_argument("--profile-directory=Profile 1")

        # Create webdriver
        self.driver = webdriver.Chrome(options=options, service=service)

    def go_to_tiktok(self):
        self.driver.get("https://www.tiktok.com")

    def login(self, driver, username, password) -> bool:
        login_successful = False

        WebDriverWait(driver=driver, timeout=60).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/button')
            )
        ).click()
        time.sleep(2)
        WebDriverWait(driver=driver, timeout=60).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="loginContainer"]/div/div/a[2]')
            )
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
        ).send_keys(username)
        time.sleep(2)
        WebDriverWait(driver=driver, timeout=60).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="loginContainer"]/div/form/div[2]/div/input')
            )
        ).send_keys(password)
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

    # Pause all videos on the website to ensure bot can access watch them in full
    def pause_videos(self):
        self.driver.execute_script(
            'videos = document.querySelectorAll("video"); for(video of videos) { video.currentTime=0; video.pause(); }'
        )

    # Clicks the like button ti like the current video
    def like_video(driver):
        WebDriverWait(driver=driver, timeout=60).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/button[1]',
                )
            )
        ).click()

    # Clicks the next button to go forward a video
    def next_video(driver):
        WebDriverWait(driver=driver, timeout=60).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[2]/div[3]/div[1]/button[3]',
                )
            )
        ).click()

    # Clicks the back button to go back a video
    def previous_video(driver):
        WebDriverWait(driver=driver, timeout=60).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[2]/div[3]/div[1]/button[2]',
                )
            )
        ).click()

    # Returns url of first video clicked
    def get_first_vid_url(self):
        self.click_first_video()
        return self.driver.current_url

    # Click on first post to enter mobile like viewing state
    def click_first_video(self):
        WebDriverWait(driver=self.driver, timeout=60).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[1]',
                )
            )
        ).click()

    # Gets and returns tags associated with the current video
    def get_current_video_tags(driver):
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
    
    def watch_n_minutes(low, high):
        return np.random.randint(low=low, high=high)

    def watch_n_videos(self, n, user, tags):
        for i in range(n):
            watch_or_skip = watch_or_skip(self.driver, user, tags):
            if watch_or_skip:
                pass
            time.sleep(5)
            self.next_video()

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

    def watch_or_skip(driver, user, tags):
        is_of_interest = False
        for interest in user.get_interests():
            for tag in tags:
                if interest.lower() == tag.lower():
                    is_of_interest = True
                    break
            if is_of_interest:
                return is_of_interest

    def collect_video_info(self):
        current_vid = self.driver.current_url
        tags = self.get_current_video_tags()
