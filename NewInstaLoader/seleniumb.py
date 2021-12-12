from second import *
from selenium import webdriver


def selstart(user,password):
    driver = webdriver.Firefox()
    driver.get("htpps://www.instagram.com")