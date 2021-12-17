from second import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random


path = r""

driver = webdriver.Firefox(executable_path=path)

# selenium start, mostly not used.
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


def FollowRandom(username,password):
    # gets lists of the people we are following.
    profile = instaloader.Profile.from_username(L.context, username)
    following_list = []
    for follower in profile.get_followees():
        following_list.append(follower.username)

    # IG Login:
    driver.get("https://www.instagram.com/accounts/login/?next=%2F&source=logged_out_half_sheet")

    sleep(3)
    username1 = driver.find_element_by_name("username")
    username1.send_keys(username)
    sleep(0.5)

    passW = driver.find_element_by_name("password")
    passW.send_keys(password)
    sleep(0.5)

    driver.find_element_by_xpath('//button[@type="submit"]').click()

    # Following Loop:
    # gets a random person we are following and accesses their following.

    randomnum = random.randint(0, 3) # need to add randomnum, seems to be buggy will check soon.
    person = following_list[randomnum]
    print(person)
    followinglistperson = Following(person, person)
    print(followinglistperson)
    # loop start
    followvartemp = 0 # just a tempvar
    amount = 10 # amount of people you want to follow
    while followvartemp < amount:
        # removes people we already follow from the list.
        followlist = ldiffer(followinglistperson, following_list)
        driver.get("https://www.instagram.com/" +followlist[followvartemp])
        sleep(2)
        driver.find_element_by_xpath("//*[text()='Follow']").click()
        file = open("followed.txt", "a+") 
        file.write(followlist[followvartemp])
        file.write("\n")
        file.close()
        sleep(random.randint(2, 8))
        followvartemp = followvartemp + 1
        

 # need to add a few cython parts to make it work more efficently, currently its pretty slow.