# -*- coding: utf-8 -*-
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# Define class
class TaoBaoInfo:

    # Define construct method
    def __init__(self):
        url = 'https://login.taobao.com/member/login.jhtml'
        self.url = url

        options = webdriver.ChromeOptions()
        # Speed the website response without loading images
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        # Use developer mode to avoid to be detected selenium
        options.add_experimental_option('excludeSwitches', ['enable-automation'])

        self.browser = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
        # Set timeout
        self.wait = WebDriverWait(self.browser, 10)

    # Login
    def login(self):

        # Use get method to open the website
        self.browser.get(self.url)

        # Wait password text area and login button display
        password_login = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.qrcode-login > '
                                                                                          '.login-links > '
                                                                                          '.forget-pwd')))
        password_login.click()

        # Wait weibo login button display
        weibo_login = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.weibo-login')))
        weibo_login.click()

        # Wait user account text area of weibo display
        weibo_user = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.username > .W_input')))
        weibo_user.send_keys(weibo_username)

        # Wait password text area of weibo display
        weibo_pwd = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.password > .W_input')))
        weibo_pwd.send_keys(weibo_password)

        # Wait login button display
        submit = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.btn_tip > a > span')))
        submit.click()

        # Get the user name and verify login result
        tao_bao_name = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, '.site-nav-bd > '
                                                                                        'ul.site-nav-bd-l > '
                                                                                        'li#J_SiteNavLogin > '
                                                                                        'div.site-nav-menu-hd > '
                                                                                        'div.site-nav-user > '
                                                                                        'a.site-nav-login-info-nick '
                                                                                        '')))
        # print the user name
        print(tao_bao_name.text)


# Steps：
# 1. Download Chrome Browser https://www.google.com/chrome/
# 2. Check the version of Chrome and download the ChromeDriver with same version:
#           http://chromedriver.storage.googleapis.com/index.html
# 3. Fill in the absolute path of ChromeDriver
# 4. Execute command pip install selenium
# 5. Open https://account.weibo.com/set/bindsns/bindtaobao and bind the taobao account

if __name__ == "__main__":

    resources_path = os.path.abspath('..') + "/resources"

    chrome_driver_path = "/Users/bird/Desktop/chromedriver"
    weibo_username = "15626145270"
    weibo_password = "zsqzttlxh...."

    a = TaoBaoInfo()
    a.login()

