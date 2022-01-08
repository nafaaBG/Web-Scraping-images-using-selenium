__author__      = "BOUGRAINE Nafaa"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver as wb
from selenium.webdriver import ActionChains
import time, urllib.request
import os 
import logging
import argparse
import uuid

from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
logging.basicConfig(level=logging.DEBUG)

class MyScrapper :
    global driver
    def __init__(self, user, pwd, page_name, number, folder_name):
        self.folder_name = folder_name
        self.user = user
        self.pwd = pwd
        self.page_name = page_name
        self.number = int(number)
        self.driver = driver

    def start_connection(self):
        driver.get("https://www.instagram.com/")
        time.sleep(5)
        username=driver.find_element_by_css_selector("input[name='username']")
        password=driver.find_element_by_css_selector("input[name='password']")
        username.clear()
        password.clear()
        username.send_keys(self.user)
        password.send_keys(self.pwd)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
        #save your login info?
        time.sleep(10)
        driver.find_element_by_xpath("//button[contains(text(), 'Plus tard')]").click()
        #turn on notif
        time.sleep(10)
        driver.find_element_by_xpath("//button[contains(text(), 'Plus tard')]").click()
        #searchbox
        time.sleep(5)
        searchbox=driver.find_element_by_css_selector("input[placeholder='Rechercher']")
        searchbox.clear()
        searchbox.send_keys(self.page_name)
        time.sleep(5)
        searchbox.send_keys(Keys.ENTER)
        time.sleep(5)
        searchbox.send_keys(Keys.ENTER)
        time.sleep(5)
        # will be used in the while loop

#scroll down
    def fetch_posts(self):
        posts = []
        scrolldown=driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
        match=False
        while(match==False):
            last_count = scrolldown
            time.sleep(1)
            scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
            divs = driver.find_elements(By.CLASS_NAME, 'KL4Bh')     
            for div in divs:
                img = div.find_element(By.TAG_NAME, 'img')
                post = img.get_attribute('src')
                if (post not in posts and len(posts) < self.number):
                    posts.append( post ) 
            if last_count==scrolldown:
                match=True
        try: 
            os.mkdir(self.folder_name)    
        except: 
            print("Folder Exist with that name!")
            self.folder_name = input("Enter another Folder Name:- ")
        return(posts)

    def download_images(self, posts): 
        x=0
        for post in posts:
            x=x+1
            driver.get(post)
            urllib.request.urlretrieve( post, './'+self.folder_name+'/{}.jpg'.format("img"+str(x)))


             

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Runnnig...")
    parser.add_argument(
        "--user-email",
        "-U",
        help="Enter your username to login",
    )
    parser.add_argument(
        "--password",
        "-P",
        help="Enter your password to login",
        default="tracing",
    )
    parser.add_argument(
        "--instagram-page", 
        "-I",
        default="", 
        help="Enter the name of the page that you wanna scrap !!"
    )

    parser.add_argument("--number-images",
        "-N",
        default=20, 
        type=int, 
        help="Enter the number of images you want !!"
    )
    parser.add_argument("--export-folder",
        "-E",
        default=str(uuid.uuid4().hex),
        help="enter a enter a file name to create and store the scrapped images in this file."
    )
    args = parser.parse_args()
    images = MyScrapper(args.user_email,args.password,args.instagram_page,args.number_images,args.export_folder)
    images.start_connection()
    posts = images.fetch_posts()
    images.download_images(posts)
