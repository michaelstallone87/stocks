import os
import time
from selenium import webdriver
import pandas as pd
from os.path import expanduser
import shutil


home = expanduser("~")
file = rf"{home}/Downloads/statusinvest-busca-avancada.csv"

#Config DataFrame Procedure
def DownloadDF(url, file):
    driver = webdriver.Chrome('lib/chromedriver')  # Optional argument, if not specified will search path.
    driver.get(url);
    time.sleep(5) # Let the user actually see something!
    try:
        publish_close = driver.find_element_by_class_name('btn-close')
        publish_close.click()
        search_box = driver.find_element_by_xpath('//div/button[contains(@class,"find")]')
        search_box.click()
        time.sleep(2) # Let the user actually see something!
        download_button = driver.find_element_by_xpath('//div/a[contains(@class,"btn-download")]')
        time.sleep(2)
        if os.path.exists(file):
            os.remove(file)
        else:
            print("The file does not exist")
        download_button.click()
        time.sleep(2)
        driver.quit()
    except:
        driver.quit()

#Download DataFrame FII:
fii = 'https://statusinvest.com.br/fundos-imobiliarios/busca-avancada'
DownloadDF(fii, file)
df = shutil.move(file, r"data/fii.csv")
df_fii = pd.read_csv(df, sep=';')

#Download DataFrame Stocks:
stocks = 'https://statusinvest.com.br/acoes/busca-avancada'
DownloadDF(stocks, file)
df = shutil.move(file, r"data/stocks.csv")
df_stocks = pd.read_csv(df, sep=';')
