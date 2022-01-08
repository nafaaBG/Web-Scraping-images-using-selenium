## Web Scraping images using Selenium and Python
![N|Solid](https://d33wubrfki0l68.cloudfront.net/c82a4677a33f15b40da09166e14505dffc14eb1d/890b9/blog/selenium-python/header_selenium_python_hu858c713577cea0e612703bbde5071118_85692_1200x0_resize_catmullrom_2.png)
## A propos de ce document
This is a markdown document about Web scraping images using Selenium and python. The document summarizes the presentation which has been divided in 2 parts: general presentation and workshop (the workshop is the tutorial in the table of contents).
Author : 
- Nafaa BOUGRAINE [Linkedin](https://www.linkedin.com/in/nafaa-bougraine/) <nafaa.bougraine@um5r.ac.ma>  

Markdown is a lightweight markup language based on the formatting conventions
that people naturally use in emails.
As written by [John Gruber] on the [Markdown site][df1]

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions. 

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
    + [_Download webdriver:_](#download-webdriver)
    + [_Installing the required libraries:_](#installing-the-required-libraries)
    + [_Importing the libraries :_](#importing-the-libraries)
- [Setting the PATH code :](#setting-the-PATH-code)
- [Get the website :](#get-the-website)
- [Login and Searchbox handling :](#login-and-Searchbox-handling)
- [Scroll down the profile :](#scroll-down-the-profile)
- [Get the URL posts :](#get-the-URL-posts)
- [Download all of the posts :](#download-all-of-the-posts)
- [Running :](#running)
- [Conclusion :](#conclusion)



## Introduction
Selenium is a Python library and tool used for automating web browsers to do a number of tasks. One of such is web-scraping to extract useful data and information that may be otherwise unavailable.
![N|Solid](https://bs-uploads.toptal.io/blackfish-uploads/uploaded_file/file/253814/image-1589553330104-3887f4e1986e94fea6b7b2fbf7a2fbcb.png)
##### _Why using Selenium?_
As we know that many tools can be used to scraping data from a website, and the three most popular from them are Scrapy, Beautifulsoup, and Selenium. However, each of them has the special ability for their action to scrape a website.
Selenium is a powerful tool for scraping. It can handle automation in a complex way. For example, we need to log in to our Instagram account to scraping Instagram’s website. And surprisingly, selenium can handle it such as log in to our Instagram account automatically.
Selenium is useful when you have to perform an action on a website such as :
- *Clicking on buttons*
- *Filling forms*
- *Scrolling*
- *Taking a screenshot*


### Installation
We will use Chrome in our example, so make sure you have it installed on your local machine:
##### _Download webdriver_
One of the tools that we must prepare to run the selenium program is webdriver (for Chrome) or geckodriver (for Firefox). You can download it from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) (for Chrome user).
##### _Installing the required libraries_
First, we must install a selenium library on our terminal such as the code below:
```
pip install selenium
```
Once it has been done, then we must install some python libraries required such as time and requests like the code below:
```
pip install time
```
and
```
pip install requests
```
Great! Our scraping environment has been prepared, and let’s code!
##### _Importing the libraries_
Here the code about importing the required libraries for scraping using selenium:
```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time, urllib.request
import requests
import os 
import argparse
```
### Setting the PATH code
The PATH code is the code that aims to connect our code with the browser. Here the code about PATH is below:
```sh
# Configure environment variables path for chromedriver.exe
PATH = r"C:\Users\DELL\Desktop\Scrapping photos clothes\chromedriver.exe"
driver = webdriver.Chrome(PATH)
```
Or alternatively, if you saved your webdriver inside the root folder, you can simply type the following and skip the file_path specification:
```sh
driver = webdriver.Chrome()
```
### Start Connection and Login
#### Get the website
After coding the PATH variable, then we must get Instagram’s website which is our scraping target. So, the code is below:
```sh
# Navigate to Instagram page
driver.get("https://www.instagram.com/")
```
>This will launch Chrome in headfull mode (like regular Chrome, which is controlled by our Python code). You should see a message stating that the browser is controlled by automated software.
#### Login and Searchbox handling
Since we’ve found the primary page of our Instagram account named home, then we must login with username and password,after that we must go to the Instagram account target by type the name of our Instagram account target in the search box located at the top of the display.
Then, we must get the element of the search box to fill the blank box automatically.
```sh
#login and searchbox function
    def start_connection(self):
        driver.get("https://www.instagram.com/")
        time.sleep(3)
        username=driver.find_element_by_css_selector("input[name='username']")
        password=driver.find_element_by_css_selector("input[name='password']")
        username.clear()
        password.clear()
        username.send_keys(self.user)
        password.send_keys(self.pwd)
        driver.find_element_by_css_selector("button[type='submit']").click()
        #save your login info?
        time.sleep(5)
        driver.find_element_by_xpath("//button[contains(text(), 'Plus tard')]").click()
        #turn on notif
        time.sleep(5)
        driver.find_element_by_xpath("//button[contains(text(), 'Plus tard')]").click()
        #searchbox
        time.sleep(5)
        searchbox=driver.find_element_by_css_selector("input[placeholder='Rechercher']")
        searchbox.clear()
        searchbox.send_keys(self.page_name)
        time.sleep(3)
        searchbox.send_keys(Keys.ENTER)
        time.sleep(3)
        searchbox.send_keys(Keys.ENTER)
        time.sleep(3)
```
>The code above explains that we started by login to our Instagram account, then we handled the search box automatically by creating the searchbox variable.
#### Scroll down the profile
Since we have the profile page for the target user, we must think that we have already scraped this page soon. However, we must scroll down the page automatically first before.
After we need to get these URL of images which are posted in the instagram page.
First, we must create the empty box which is used to accommodate all the URL posts named posts.
Then, we create the divs variable which is to get all the elements that have the class name “KL4Bh”.  Then, create the for loop function to get all the URL posts. 
Thus, create a folder so that we can group the downloaded images by following the code below.
```sh
#scroll down and fetch links and create the folder
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
```




#### Download all of the posts
Lastly, we must download all of the posts on there, and save them to our directory. So, the code is in below:
```
    def download_images(self, posts): 
        x=0
        for post in posts:
            x=x+1
            driver.get(post)
            urllib.request.urlretrieve( post, './'+self.folder_name+'/{}.jpg'.format("img"+str(x)))
```
**The Main Function :**
```
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
```
#### Running
Open terminal in the directory of scraper.py and enter:
In the first argument enter your instagram username after typing -U or -user-email, in the second enter the password after typing -P or -password, in the third enter the name of the page you want to scrape after typing -I or -instagram-page, in the fourth argument enter the number of images you want to save after typing -N or -number-images it must be an integer, and the last argument enter a file name after typing -E or -export-folder to create and store the scrapped images in this file.
```
python scraper.py -U  "user@gmail.com" -P "Your password" -I "The page" -N 60 -E "file"
```
Go grab a cup of coffee while waiting... oh wait, it's already done!
>For more informations run this command :
```
python scraper.py --help
```
### Conclusion
Finally, we have got all about the code completely in here. Here the code:
```
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
```

**The end ! Thank you all** 

***NOTE:***
Web Scraping from many websites is Illegal.
This project is just for Learning and Fun.

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [git]: <https://git-scm.com>
   [git-setup-server]: <https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Original-article-inspired-from]: <https://cs.brown.edu/courses/csci1320/tutorials/cs132-git-markdown-tutorial/markdown-git.html#git>

