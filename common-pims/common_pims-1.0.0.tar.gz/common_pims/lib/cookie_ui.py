#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ChromeOptions  #这个包用来规避被检测的风险

#pims test 非单点登录
def userlogin(url_c, username,pwd):
    #点击产品名称

    option = webdriver.ChromeOptions()
    option.add_argument('--no--sandbox')  # 沙箱机制
    option.add_argument('headless')  #无界面模式
    option.add_experimental_option('useAutomationExtension', False)
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    # driver=webdriver.Chrome(executable_path=driver_path,options=option)  #初始化路径，规避检测
    driver = webdriver.Chrome(options=option)
    # driver.excute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument"),{}

    driver.get(url_c)
    driver.maximize_window()
    sleep(0.3)
    driver.implicitly_wait(10)  # 如果网页没有加载完，避免出现加载超时的报错最多让他加载10秒
    driver.find_element_by_xpath("//*[@id='userName']").send_keys(username)
    driver.find_element_by_xpath("//*[@id='passWord']").send_keys(pwd)
    sleep(0.3)
    driver.find_element_by_xpath("//button[text()='登录']").click()
    sleep(0.5)
    driver.refresh()  # 刷新
    sleep(0.3)
    cookies = driver.get_cookies()  # 获取cookie信息
    sleep(0.3)
    srts = ".."
    # print(cookies)
    for cookie in cookies:
        srts = "%s'%s':'%s'," % (srts, cookie["name"], cookie["value"])
    srts=srts.replace('..', '')
    cookie=eval('{'+srts+'}')

    # print(cookie)
    return cookie

#
# url_c='http://prj.chinasoftinc.com/prj_test/index.jsp'
# username=2430
# pwd=123456
# userlogin(url_c, username,pwd)