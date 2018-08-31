from module.driver import driver
from module.generator import gen
import time
if __name__ == "__main__":

    while True:

        generat = gen()
        mail = generat.get_mail()
        name = generat.get_nick()
        specialty = generat.get_spec()
        web_driver = driver()
        web_driver.register(name, specialty, mail)
        for i in range(5):
            web_driver.submit(i)
        time.sleep(3)
        web_driver.close()
        acc = open("account.txt", 'a')
        acc.write("email:{0}, name:{1}, spec:{2}\n".format(
            mail, name, specialty))
        acc.close()
        print("cooldown 10")
        time.sleep(10)
