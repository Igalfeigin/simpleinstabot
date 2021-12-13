from second import *
from seleniumb import *

#<Important Variables>
username = ""
password = ""
path = r"C:\Users\igalg\Downloads\geckodriver\geckodriver.exe"

# load the selenium, enter the account
# selstart()


# login.
L.login(username, password)

#follows random people.
FollowRandom(username,password,username,path)


#if using the unfollow, a list of poeple you dont want to be unfollowed.  (W.I.P)
starpeople = ['mkbhd','carthrottle','pewdiepie']

