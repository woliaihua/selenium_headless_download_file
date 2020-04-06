#!/usr/bin/python
# _*_ coding:utf-8 _*_
# Time : 2018/8/14 14:57
"""
当前成功的谷歌浏览器版本 80.xxxxx
如果在当前页面打开新标签页，点击下载无头模式是无效的（因为切换新标签页面之后chrome_options就失效了）。因此需要重新实例化对象再使用driver.get(url)去下载"""

import time
from selenium.webdriver import Chrome
from selenium import webdriver
download_location = 'E:\\'
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory': download_location,
         'download.prompt_for_download': False,
         'download.directory_upgrade': True,
         'safebrowsing.enabled': False,
         'safebrowsing.disable_download_protection': True}

chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument("--headless")
driver = Chrome(options=chrome_options)
driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')

params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_location}}
command_result = driver.execute("send_command", params)
# print("response from browser:")
# for key in command_result:
#     print("result:" + key + ":" + str(command_result[key]))

# 这里是随便选了一个可以下载的连接，无心骚扰。
driver.get("http://www.yundama.com/apidoc/YDM_SDK.html")
clone_box = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/p[11]/a')
clone_box.click()
time.sleep(10)
driver.quit()