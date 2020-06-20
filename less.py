#auto less secure by sm0usy
#fb.me/GueHuman
#pertama kali code dipython, maap masih berantakan
import logging, selenium, time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

def less_secure(em):
    options = webdriver.ChromeOptions();
    options.add_experimental_option('excludeSwitches',['enable-logging']);

    ems = em.strip().split('|', 1)
    driver = webdriver.Chrome('chromedriver.exe', options=options)
    driver.get('https://www.typing.com/student/signup')
    try:
        driver.find_element_by_xpath('//*[@id="app"]/div/div/main/div/div[1]/div[1]/a').click()
        # INPUT EMAIL
        put_email = driver.find_element_by_xpath('//*[@id="identifierId"]')
        put_email.clear()
        put_email.send_keys(ems[0])
        time.sleep(3)
        # NEXT
        driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()
        time.sleep(3)
        try:
            # INPUT PASSWORD
            put_password = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, 'password')))
            put_password.clear()
            put_password.send_keys(ems[1])
            time.sleep(1)
            # NEXT
            driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click()
            time.sleep(3)
            try:
                driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
                driver.close()
                return print('[WRONG PASSWORD] => ' + ems[0])
            except NoSuchElementException:
                pass
            try:
                driver.find_element_by_xpath('//*[@id="accept"]').click()
            except NoSuchElementException:
                pass
            time.sleep(2)
            driver.get('https://myaccount.google.com/lesssecureapps?pli=1')
            time.sleep(3)
            if driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[3]/c-wiz/div/div[3]/div[1]/div/div/div/div[2]/div').get_attribute("aria-checked") == 'false':
                driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div[3]/c-wiz/div/div[3]/div[1]/div/div/div/div[2]/div').click()
            else:
                pass
            print('[OK] => ' + ems[0])
        except NoSuchElementException:
            print('[WRONG EMAIL] => ' + ems[0])
    except NoSuchElementException:
        print('[ERROR] => ' + ems[0])
    driver.close()
        
list = open('list.txt', 'r').readlines()
list = [line.replace('\n', '') for line in list]


for em in list:
    less_secure(em)
