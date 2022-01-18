# Imports
from instaloader.structures import Profile
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
from typing import Counter
import instaloader
from bs4 import BeautifulSoup



# imports path
L = instaloader.Instaloader()
path = r"X:\geckodriver.exe"

username = ""
password = ""

L.login(username,password)

# Starting Instaloader And WebDriver
driver = webdriver.Firefox(executable_path=path)

# Main Code 
class Bot():
    def FollowingCount(usermame):
        Profile = instaloader.Profile.from_username(L.context, username)
        return len(set(Profile.get_followees()))

    def FollowersCount(usermame):
        Profile = instaloader.Profile.from_username(L.context, username)
        return len(set(Profile.get_followers()))

    # returns list differnece
    def ldiffer(list1, list2):
        list_difference = []
        for item in list1:
            if item not in list2:
                list_difference.append(item)
        return list_difference

    # gets profile followers and returns a list.
    def Followers(username,profile):
        
        # gets all profile data
        profile = instaloader.Profile.from_username(L.context, profile)

        follow_list = []
        count = 0
        for follower in profile.get_followers():
            follow_list.append(follower.username)
            file = open("followers.txt", "a+")
            file.write(follow_list[count])
            file.write("\n")
            file.close()
            count = count + 1
        return follow_list
    
    # gets profile following and returns a list.
    def Following(username, profile):
        
        # gets all profile data
        profile = instaloader.Profile.from_username(L.context, profile)

        following_list = []
        count = 0
        
        for follower in profile.get_followees():
            following_list.append(follower.username)
        '''
            file = open("following.txt", "a+")
            file.write(following_list[count])
            file.write("\n")
            file.close()
            count = count + 1
        '''
        return following_list
        
    def fBack(user):
        profile = instaloader.Profile.from_username(L.context, user)

        follow_list = []
        followu = 0
        for follower in profile.get_followers():
            follow_list.append(follower.username)
            followu = followu + 1

        following_list = []
        following = 0
        for follower in profile.get_followees():
            following_list.append(follower.username)
            following = following + 1

        return Bot.ldiffer(following_list, follow_list)
    
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
        followinglistperson = Bot.Following(person, person)
        print(followinglistperson)
        # loop start
        followvartemp = 0 # just a tempvar
        amount = 20 # amount of people you want to follow
        while followvartemp < amount:
            # removes people we already follow from the list.
            followlist = Bot.ldiffer(followinglistperson, following_list)
            driver.get("https://www.instagram.com/" +followlist[followvartemp])
            sleep(2)
            driver.find_element_by_xpath("//*[text()='Follow']").click()
            file = open("followed.txt", "a+") 
            file.write(followlist[followvartemp])
            file.write("\n")
            file.close()
            sleep(random.randint(2, 8))
            followvartemp = followvartemp + 1
        
    def FollowAccount(username,password,account,amount):
        try:
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

            # Loop, check amount and choose the
            followvartemp = 0
            followlistperson =  Bot.Following(account, account)
            followinglist = followlistperson[0:amount]
            followlist = Bot.ldiffer(following_list, followinglist)

            while followvartemp < amount:
                driver.get("https://www.instagram.com/" + followlist[followvartemp])
                sleep(3)
                driver.find_element_by_xpath("//*[text()='Follow']").click()
                #file = open("followed.txt", "a+") 
               # file.write(followlist[followvartemp])
                #file.write("\n")
                #file.close()
                sleep(random.randint(5, 15))
                followvartemp = followvartemp + 1  
        except:
            print("Error Following")
    
    def FFR(person):
        FollowingList =Bot.Following(person, person)
        list = []
        temp = 0 
        while temp < len(FollowingList):
            driver.get("https://www.instagram.com/" + FollowingList[temp])
            soup = BeautifulSoup(driver.page_source,"html.parser")
            driver.quit()

            for title in soup.select("._h9luf"):
                    follower = title.select("._fd86t")[1]['title']
                    following = title.select("._fd86t")[2].text
            if following > follower:
                list.append(FollowingList[temp])
        return list 

    def Unfollow(filename):
        pass

    # Unfollowing
    def unfollowfucks(username, password,amount):
        try:
            driver.get("https://www.instagram.com/accounts/login/?next=%2F&source=logged_out_half_sheet")

            sleep(3)
            username1 = driver.find_element_by_name("username")
            username1.send_keys(username)
            sleep(0.5)

            passW = driver.find_element_by_name("password")
            passW.send_keys(password)
            sleep(0.5)

            driver.find_element_by_xpath('//button[@type="submit"]').click()
            sleep(3)
            
            list = Bot.Following(username,username)
            # making the followers txt into a list
            #f = open("followers.txt","r")
            #lst = []
            #for x in f:
            #    lst.append(x)
            #print(lst)
            # making the starpeople txt into a list
            #f2 = open("starpeople.txt" , "r")
            #lst2 = []
            #for y in f2:
            #    lst2.append(y)

            # make sure the usernames are exact
            #lst3 = Bot.ldiffer(lst , lst2)

            temp = 0
            while temp < amount:
                driver.get("https://www.instagram.com/" + list[temp])
                sleep(2)
                x = driver.find_elements_by_css_selector("[aria-label=Following]")
                x[0].click()
                driver.find_element_by_xpath("//*[text()='Unfollow']").click()
                #only need to add the actual button pressing

                sleep(random.randint(5, 15))    
                temp = temp + 1
        except:
            print("Error Unfollowing")

    # Unfollowing
    def unfollowfucks2(username, password,amount):
        try:
            list = Bot.Following(username,username)
            temp = 0
            while temp < amount:
                driver.get("https://www.instagram.com/" + list[temp])
                sleep(2)
                x = driver.find_elements_by_css_selector("[aria-label=Following]")
                x[0].click()
                driver.find_element_by_xpath("//*[text()='Unfollow']").click()
                #only need to add the actual button pressing

                sleep(random.randint(5, 15))    
                temp = temp + 1
        except:
            print("Error Unfollowing")

    def FollowAccount2(username,password,account,amount):
        try:
            # gets lists of the people we are following.
            profile = instaloader.Profile.from_username(L.context, username)
            following_list = []
            for follower in profile.get_followees():
                following_list.append(follower.username)

            # Loop, check amount and choose the
            followvartemp = 0
            followlistperson =  Bot.Following(account, account)
            followinglist = followlistperson[0:amount]
            followlist = Bot.ldiffer(following_list, followinglist)

            while followvartemp < amount:
                driver.get("https://www.instagram.com/" + followlist[followvartemp])
                sleep(3)
                driver.find_element_by_xpath("//*[text()='Follow']").click()
                sleep(random.randint(5, 15))
                followvartemp = followvartemp + 1  
        except:
            print("Error Following")