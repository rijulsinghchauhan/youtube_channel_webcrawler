import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = webdriver.ChromeOptions()
driver = webdriver.Chrome("chromedriver.exe",  options=options)
serch_url="https://www.youtube.com/results?search_query=openinapp.co"
driver.get(serch_url)
time.sleep(3)
# "Automatic Scrolling"
scroll_height=0
scroll_start=0
for i in range(120):
    scroll_start=scroll_height
    scroll_height+=1000
    driver.execute_script(f"window.scrollTo({scroll_start}, {scroll_height})")
    time.sleep(3)
channel_xpath="//yt-formatted-string//a"
channel_select_x = driver.find_elements(By.XPATH, channel_xpath)
links = [elem.get_attribute('href') for elem in channel_select_x]
youtube_urls = [i for j, i in enumerate(links) if j % 2 != 0]
# "Creating CSV"
df = pd.DataFrame(youtube_urls, columns =['youtube_urls'])
df.to_csv("Youtube_channel_list.csv",index=False)
driver.quit()