#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "http://www.ncd.co.jp"

options = Options()
options.add_argument('--headless')

#Chromeのドライバを得る
browser = webdriver.Chrome(chrome_options=options)
#暗黙的な待機を最大3秒行う
browser.implicitly_wait(3)
# URLを読み込む
browser.get(url)
# 画面をキャプチャしてファイルに保存
browser.save_screenshot("ncd.png")
# ブラウザを終了
browser.quit()