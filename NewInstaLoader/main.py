from second import *
from seleniumb import *

#<Important Variables>
username = ""
password = ""
path = r""


# login.
L.login(username, password)

#follows random people.
FollowRandom(username,password)


#if using the unfollow, a list of poeple you dont want to be unfollowed.  (W.I.P)
starpeople = ['mkbhd','carthrottle','pewdiepie']

