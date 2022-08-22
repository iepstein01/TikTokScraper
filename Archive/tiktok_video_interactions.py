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
import time


def like_video(driver):
    WebDriverWait(driver=driver, timeout=60).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                '//*[@id="app"]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/button[1]',
            )
        )
    ).click()


def next_video(driver):
    WebDriverWait(driver=driver, timeout=60).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                '//*[@id="app"]/div[2]/div[3]/div[1]/button[3]',
            )
        )
    ).click()


def previous_video(driver):
    WebDriverWait(driver=driver, timeout=60).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                '//*[@id="app"]/div[2]/div[3]/div[1]/button[2]',
            )
        )
    ).click()
