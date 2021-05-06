import json
import time
import pandas as pd
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(5)
baseUrl = "https://www.cowin.gov.in/home"
pincode = "415612"
Filled = [' NA ', ' Booked ']


def check_avail():
    driver.get(baseUrl)
    driver.find_element_by_xpath('//*[@id="mat-input-0"]').send_keys(pincode)
    search_btn = driver.find_element_by_xpath('/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[2]/div[1]/div/button')
    search_btn.click()

    for i in range (1,99999):
        for j in range (1,8):
            status = driver.find_element_by_xpath('/html/body/app-root/div/app-home/div[2]/div/appointment-table/div/div/div/div/div/div/div/div/div/div/div[2]/form/div/div/div[6]/div/div/div/div[1]/div/div/div[2]/ul/li[' + str(j) + ']/div/div/a')
            # print(status.get_attribute('text'))
            if status.get_attribute('text') not in Filled:
                print("\n\nSLOTS AVAILABLE!\n\n")
                driver.close()
                exit()

    print("\n\n Slots currently not available. Try again later. \n")
    


if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--pincode", required=True, help="Please specify your pincode")
    args = vars(ap.parse_args())

    pincode = args["pincode"]

    while True:
        check_avail()
        # driver.close()
        time.sleep(30)