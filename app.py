import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import loggin_data as data
from config import *


def app(file, twit_link):
    def loggin_button_twitter():
        login_button = driver.find_element('xpath',
                                           '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
        login_button.click()

    def input_login_data():
        email_input = driver.find_element('xpath',
                                          '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label')
        email_input.send_keys(data.loggings[data_counter])
        time.sleep(5)
        email_input.send_keys(Keys.ENTER)

    def input_password_data():
        password_input = driver.find_element('xpath',
                                             '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_input.send_keys(data.passwords[data_counter])
        time.sleep(5)
        password_input.send_keys(Keys.ENTER)

    def phone_number_verif():
        phone_number = driver.find_element('xpath',
                                           '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        phone_number.send_keys(data.phones[data_counter])
        time.sleep(2)
        phone_number.send_keys(Keys.ENTER)
        time.sleep(3)

    def email_adress_verif():

        email_adress = driver.find_element('xpath',
                                           '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        email_adress.clear()
        email_adress.send_keys(data.emails[data_counter])
        time.sleep(2)
        email_adress.send_keys(Keys.ENTER)
        time.sleep(3)

    data.split_split_text(file)
    data_counter = 0
    while len(data.loggings) > data_counter:

        # creating options
        options = webdriver.ChromeOptions()
        options.add_argument('user-agent=' + random.choice(user_agents))

        # creating driver
        driver = webdriver.Chrome(executable_path='chromedriver/chromedriver', options=options)

        try:
            driver.get(url=url)
            time.sleep(3)
            loggin_button_twitter()
            time.sleep(5)
            input_login_data()
            time.sleep(3)
            input_password_data()
            time.sleep(5)
            try:
                go_to_profile = driver.find_element('xpath', '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]/div')
                go_to_profile.click()
            except:
                try:
                    phone_number_verif()
                    go_to_profile = driver.find_element('xpath',
                                                        '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[7]/div')
                    go_to_profile.click()
                except:
                    email_adress_verif()
            finally:
                driver.get(url=twit_link)
                time.sleep(5)
                like_action = driver.find_element('xpath', '//*[@id="id__al2j796lnft"]/div[3]/div/div')
                like_action.click()
            time.sleep(5)
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()
            data_counter += 1
