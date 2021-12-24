__author__      = "BOUGRAINE Nafaa"

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, urllib.request
import os 
import sys
import logging
import argparse


driver = webdriver.Chrome()
logging.basicConfig(level=logging.DEBUG)

class MyScrapper :
    global driver

    def __init__(self, user, pwd, page_name, finalScroll, folder_name):
        self.folder_name = folder_name
        self.user = user
        self.pwd = pwd
        self.page_name = page_name
        self.finalScroll = int(finalScroll)
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
        driver.find_element_by_css_selector("button[type='submit']").click()
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

    def scroll_down(self):
        start = time.time()
        #driver = webdriver.Chrome()
        initialScroll = 0             
        while True:
            driver.execute_script(f"window.scrollTo({initialScroll},{self.finalScroll})")
            # this command scrolls the window starting from the pixel value stored in the initialScroll variable to the pixel value stored at the finalScroll variable
            initialScroll = self.finalScroll
            self.finalScroll += 1  
            # we will stop the script for 3 seconds so that the data can load
            time.sleep(3)
            end = time.time()
            # We will scroll for 20 seconds.You can change it as per your needs and internet speed
            if round(end - start) > 20:
                break
            # You can change it as per your needs and internet speed

    def fetch_links(self, posts = []):
        #driver = webdriver.Chrome()            
        links = driver.find_elements_by_tag_name('a')
        for link in links:
            post = link.get_attribute('href')
            if '/p/' in post:
                posts.append( post )
        try: 
            os.mkdir(self.folder_name)    
        except: 
            print("Folder Exist with that name!")
            self.folder_name = input("Enter another Folder Name:- ") 
        return(posts)

    def download_images(self, posts): 
        #driver = webdriver.Chrome()    
        download_url = ''
        for post in posts:	
            driver.get(post)
            shortcode = driver.current_url.split("/")[-2]
            time.sleep(7)
            download_url = driver.find_element_by_css_selector("img[style='object-fit: cover;']").get_attribute('src')
            urllib.request.urlretrieve( download_url, './'+self.folder_name+'/{}.jpg'.format(shortcode))
            time.sleep(5)

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
    parser.add_argument("--scrolls-number",
        "-S",
        default=1, 
        type=int, 
        help="Enter the number of scroll down to the bottom of the page you want !!"
    )
    parser.add_argument("--export-folder",
        "-E",
        help="enter a enter a file name to create and store the scrapped images in this file."
    )
    args = parser.parse_args()
    images = MyScrapper(args.user_email,args.password,args.instagram_page,args.scrolls_number,args.export_folder)
    images.start_connection()
    images.scroll_down()
    posts = images.fetch_links()
    images.download_images(posts)