from xml.etree.ElementTree import QName
from anytree import AnyNode, RenderTree
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


class User:
    def __init__(self) -> None:
        self.username = ""
        self.password = ""
        self.videos_watched = []

    def ask_intersts(self):
        interests = []
        while True:
            interest = input(
                'What are you interests? Please use single words, type "done" when finished.\n'
            )
            if interest == "done".lower():
                self.interests = interests
                print("Inputs Received and Stored")
                return
            interests.append(interest)

    def get_interests(self):
        return self.interests

    def get_login_credentials(self):
        self.username = input("Please input your username.")
        self.password = input("Please input your password.")

    def log_root_video(self, url, tags):
        self.root = AnyNode(id=url, parent=None, tags=tags)
        self.videos_watched.append(self.root)

    def log_children_video(self, url, parent, tags):
        node = AnyNode(
            id=url,
            # TODO: continue this
        )

    def render_path(self):
        RenderTree(self.root)
