from user import User
from tiktok_scraper import TikTok_Scraper

user = User()
scraper = TikTok_Scraper()
interested_videos_counter = 0
non_interested_videos_counter = 0

user.ask_intersts()
user.get_login_credentials()
scraper.create_chrome_driver()
scraper.go_to_tiktok()
# TODO: have an if statement here, if a certain element exists, don't ask to login, if not, then ask to login
# TODO: make a requirements.txt for all this to make it easier to install with pip
# scraper.login(user.username, user.password)
# print("login successful")
scraper.click_first_video()
print(scraper.get_root_vid_url())
scraper.watch_n_videos(5, user, user.get_interests())
