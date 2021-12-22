# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 12:24:48 2021

@author: Mad_ToBy
"""

import requests
from selenium import webdriver
from time import sleep
import schedule
import time
import tkinter





def get_cookie(url_, user_):
    driver = webdriver.Chrome()
    driver.get(url_)
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(user_['name'])
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(user_['password'])
    driver.find_element_by_xpath('//*[@id="login"]').click()
    sleep(2)
    cookie_ = driver.get_cookies()[3]
    driver.quit()
    return cookie_['name']+'='+cookie_['value']

def automateSign( user ):
    cookie = get_cookie('https://sso.stu.edu.cn/login?service=https%3A%2F%2Fmy.stu.edu.cn%2Fhealth-report%2Finit-stu-user', user)



    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36',
    'Cookie': cookie
    }
    data  = {
    'health':'良好',
    'familyHealth':'良好',
    'importantPersonType': 4,
    'dailyReport.afternoorBodyHeat': 36.0,
    'dailyReport.forenoonBodyHeat': 36.0,
     # 将接下来的4个空字符修改为相应的内容
    'dailyReport.currentAddr.province': '',#自己所在省
    'dailyReport.currentAddr.city': '',#所在市
    'dailyReport.currentAddr.dist': '',#所在区
    'dailyReport.currentAddr.detailAddr': '',#具体位置
    'dailyReport.hasCough': 'false',
    'dailyReport.hasShortBreath': 'false',
    'dailyReport.hasWeak': 'false',
    'dailyReport.hasFever': 'false',
    'dailyReport.exception': '',
    'dailyReport.treatment':  '',
    'dailyReport.conclusion':  '',
    'watchingInfoOutofStu.address':'' ,
    'watchingInfoOutofStu.startDate': '',
    'watchingInfoOutofStu.comment': '',
    }
    s = requests.session()
    response  = s.post(url = 'https://my.stu.edu.cn/health-report/report/saveReport.do',headers = headers, data = data)
    response.encoding = 'utf-8'
    if 'true' in response.text :
        print('successfully report')