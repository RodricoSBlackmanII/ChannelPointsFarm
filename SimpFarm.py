'''
Created on Jun 28, 2021

@author: Hitma
'''

from selenium import webdriver
import time
from datetime import datetime
from selenium.webdriver.common.by import By

d = webdriver.Chrome()

def take_to_twitch(driver):
    d.get("https://www.twitch.tv/kyootbot")
    time.sleep(7)
    login_button = d.find_element(By.XPATH, "//button[contains(@class,'ScCoreButton-sc-1qn4ixc-0 ScCoreButtonSecondary-sc-1qn4ixc-2 ffyxRu kgzEiA')]")
    login_button.click()
    
    login(d)
    
def login(driver):
    uname = "Official_shalamar"
    pword = "Radman2319"
    time.sleep(3)
    UsernameI = d.find_element(By.ID, "login-username")
    UsernameI.send_keys(uname)
    PasswordI = d.find_element(By.ID, "password-input")
    PasswordI.send_keys(pword)
    time.sleep(2)
    button_login =d.find_element(By.XPATH, "//button[contains(@data-a-target,'passport-login-button')]")
    button_login.click()
    done = input("Is it done?")
    if (done == 'Y' or 'Yes' or 'y' or 'yes'):
        print("Okay!")
        channel_farm(d)
    
def channel_farm(d):
    while datetime.now().minute not in {0, 15, 30, 45}:  # Wait 1 second until we are synced up with the 'every 15 minutes' clock
        time.sleep(1)
        
    def click_chest(driver):
        ChestE = d.find_element(By.XPATH, "//button[contains(@class,'ScCoreButton-sc-1qn4ixc-0 ScCoreButtonSuccess-sc-1qn4ixc-5 ffyxRu gjXDMG')]")
        time.sleep(5)
        ChestE.click()
        time.sleep(20)
        ChestE.click()
        global Works
        Works = True
    
    click_chest(d)
    
    while Works == True:
        time.sleep(60*15)  # Wait for 15 minutes
        Works = False
        click_chest()
        
if __name__ == '__main__':
    take_to_twitch(d)