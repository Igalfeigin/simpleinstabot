from typing import Counter
import instaloader
L = instaloader.Instaloader()

# scrapes for followers, enter username variable and password variable
# leave profile empty for for your own profile.
def Followers(username, password, profile):
    if profile == "":
        profile = username

    # get profile data   
    profile = instaloader.Profile.from_username(L.context, profile)

    # save it to a list.
    follow_list = []
    count = 0
    for follower in profile.get_followers():
        follow_list.append(follower.username)
        file = open("followers.txt", "a+")
        file.write(follow_list[count])
        file.write("\n")
        file.close()
        count = count + 1
    # print(follow_list) - used for debug
    return follow_list

# scrapes for the followees, enter username variable and password variable
# leave profile empty for your own profile
def Following(username, password, profile):
    if profile == "":
        profile = username

    # get profile data   
    profile = instaloader.Profile.from_username(L.context, profile)

    # save it to a list.
    following_list = []
    count = 0
    for follower in profile.get_followees():
        following_list.append(follower.username)
        file = open("following.txt", "a+")
        file.write(following_list[count])
        file.write("\n")
        file.close()
        count = count + 1
    # print(following_list) - used for debug
    return following_list
# finds people that dont follow back.
# enter profile name variable
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

    return ldiffer(following_list, follow_list)


def ldiffer(list1, list2):
    list_difference = []
    for item in list1:
        if item not in list2:
            list_difference.append(item)
    return list_difference
