from exec import *
from apscheduler.schedulers.blocking import BlockingScheduler

#<Important Variables>
username = ""
password = ""
path = r"X:\geckodriver.exe"

Bot.unfollowfucks(username,password,10)
Bot.FollowAccount2(username,password,"2917koko",10)

def main():
    Bot.unfollowfucks2(username,password,10)
    Bot.FollowAccount2(username,password,"2917koko",10)
    
scheduler = BlockingScheduler()
scheduler.add_job(main, 'interval', hours=1)
scheduler.start()
