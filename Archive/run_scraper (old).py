from tiktok_scraper import TikTok_Scraper
from user import User

scraper = TikTok_Scraper()
user = User()
interested_videos_counter = 0
non_interested_videos_counter = 0



def watch_n_minutes(low, high):
    return np.random.randint(low=low, high=high)

def watch_n_videos(driver, n, user, tags):
    for i in range(n):
        watch_or_skip = watch_or_skip(driver, user, tags):
        if watch_or_skip:
            
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

def watch_or_skip(driver, user, tags):
    is_of_interest = False
    for interest in user.get_interests():
        for tag in tags:
            if interest.lower() == tag.lower():
                is_of_interest = True
                break
        if is_of_interest:
            return is_of_interest

def collect_video_info(driver):
    current_vid = driver.current_url
    tags = relevant_tags()



# Watch 5 videos
watch_n_videos(driver, 5)


driver.quit()