from second import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


path = r"C:\Users\igalg\Downloads\geckodriver\geckodriver.exe"

driver = webdriver.Firefox(executable_path=path)


def selstart(user,password,path):
    
    driver.get("https://www.instagram.com/accounts/login/?next=%2F&source=logged_out_half_sheet")

    sleep(3)

    username = driver.find_element_by_name("username")
    username.send_keys(user)
    sleep(0.5)
    passW = driver.find_element_by_name("password")
    passW.send_keys(password)
    sleep(0.5)

    driver.find_element_by_xpath('//button[@type="submit"]').click()

    # now that it has entered the account successfully, we can do a bunch of functions.
    
def FollowRandom(username,password,profile,path):

    followerlist = Followers(username,password,profile)
    followinglist = Following(username,password,profile)

    selstart(username,password,path)
    followvartemp = 0
    driver.get("https://www.instagram.com/" + followinglist[1]) 
    # logs in , but then reloads and loses the data, need to do relogin here and add an if statment to the gui