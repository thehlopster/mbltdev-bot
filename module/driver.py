from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
import random as rand


class driver:
    otvet = ("dig", "quest@95.163.108.79:10022",
             "d13bbbd92b83ddaad994a12bd9d20dfba5fff139", "http://q1.mbltdev.ru/q.webp", "0")
    url_start = "https://mbltdev.ru/ru/quiz"

    def __init__(self):
        print("init driver.", end="")
        self.driver = webdriver.Firefox(
            executable_path=r'C:\driver\geckodriver.exe')
        print("..ok")
        print("start driver.", end="")
        self.driver.get(self.url_start)
        print("..ok")

    def register(self, username, spec, email):
        driver = self.driver
        username_e = driver.find_element_by_id("id_name")
        username_e.send_keys(username)
        username_e = driver.find_element_by_id("id_position")
        username_e.send_keys(spec)
        username_e = driver.find_element_by_id("id_email")
        username_e.send_keys(email, Keys.ENTER)
        print("all done")
        print(u"\n{0}:{1}:{2}".format(username, spec, email))
        time.sleep(2)

    def submit(self, num):
        try:
            inputs = driver.find_element_by_name("answer")
            time.sleep(freez)
            inputs.send_keys(self.otvet[num], Keys.ENTER)
            print("submit {}".format(num))
        except selenium.common.exceptions.NoSuchElementException:
            print("eror: NoSuchElementException")
            pass
        except selenium.common.exceptions.StaleElementReferenceException:
            print("eror: StaleElementReferenceException")
            pass

    def close(self):
        self.driver.close()
