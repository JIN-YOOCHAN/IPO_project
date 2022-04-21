from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def crawling_total():

  chrome_options = webdriver.ChromeOptions()
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

  page_num = [i for i in range(1,999999999)]
  total_lst = []

  for i in page_num:
    driver.get(f"http://www.38.co.kr/html/fund/index.htm?o=nw&page={i}")
    driver.maximize_window()
    time.sleep(1)
    print(total_lst)

    for i in range(1,21):
      data_dic = {}
      try:
        driver.find_element_by_css_selector(f"body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(12) > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child({i}) > td:nth-child(1) > a").click()
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        name = soup.select("b")[0].text
        market = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(3) > tbody > tr:nth-child(2) > td:nth-child(2)")[0].text.split("\xa0 ")[-1].strip()
        sectors = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(3) > tbody > tr:nth-child(3) > td:nth-child(2)")[0].text.split("\xa0 ")[-1].strip() 
        price_hoping = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(6) > tbody > tr:nth-child(3) > td:nth-child(2)")[0].text.split("\xa0 ")[-1].strip() 
        price_real = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(6) > tbody > tr:nth-child(4) > td:nth-child(2) > b")[0].text.split("\xa0 ")[-1].strip() 

        try:
          inv_comp = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(11) > tbody > tr:nth-child(9) > td:nth-child(2) > table > tbody > tr > td:nth-child(2)")[0].text.split("\xa0 ")[-1].strip()
        except:
          inv_comp = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(9) > tbody > tr:nth-child(9) > td:nth-child(2) > table > tbody > tr > td:nth-child(2)")[0].text.split("\xa0 ")[-1].strip()

        stock_amount = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(6) > tbody > tr:nth-child(1) > td:nth-child(2)")[0].text.split("\xa0 ")[-1].strip()
        stock_fund = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(6) > tbody > tr:nth-child(4) > td:nth-child(4)")[0].text.split("\xa0 ")[-1].strip() 
        exec_company = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(6) > tbody > tr:nth-child(5) > td:nth-child(2) > b")[0].text.split("\xa0 ")[-1].strip()

        try:
          listing_date = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(9) > tbody > tr:nth-child(10) > td:nth-child(2) > table > tbody > tr > td:nth-child(2)")[0].text.split("\xa0 ")[-1].strip()
        except:
          listing_date = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(11) > tbody > tr:nth-child(10) > td:nth-child(2) > table > tbody > tr > td:nth-child(2)")[0].text.split("\xa0 ")[-1].strip()

        percent_newstock = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(6) > tbody > tr:nth-child(2) > td:nth-child(2)")[0].text.split("\xa0 ")[-1].strip()
        try:
          percent_invest = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(9) > tbody > tr:nth-child(7) > td:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(2)")[0].text.split("\xa0")[2].strip()
          if percent_invest == "":
            percent_invest = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(9) > tbody > tr:nth-child(7) > td:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(2)")[0].text.split("\xa0")[1].strip().replace(" 주","")
        except:
          percent_invest = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(11) > tbody > tr:nth-child(7) > td:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(2)")[0].text.split("\xa0")[2].strip()
          if percent_invest == "":
            percent_invest = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(9) > tbody > tr:nth-child(7) > td:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(2)")[0].text.split("\xa0")[1].strip().replace(" 주","")
    
        try:
          percent_personal = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(9) > tbody > tr:nth-child(7) > td:nth-child(2) > table > tbody > tr:nth-child(5) > td:nth-child(2)")[0].text.split("\xa0")[2].strip()
          if percent_personal == "":
            percent_personal - soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(9) > tbody > tr:nth-child(7) > td:nth-child(2) > table > tbody > tr:nth-child(5) > td:nth-child(2)")[0].text.split("\xa0")[1].strip().replace(" 주","")
        except:
          percent_personal = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(11) > tbody > tr:nth-child(7) > td:nth-child(2) > table > tbody > tr:nth-child(5) > td:nth-child(2)")[0].text.split("\xa0")[2].strip()
          if percent_personal == "":
            percent_personal - soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(9) > tbody > tr:nth-child(7) > td:nth-child(2) > table > tbody > tr:nth-child(5) > td:nth-child(2)")[0].text.split("\xa0")[1].strip().replace(" 주","")
            
        try:
          percent_lock_up = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(9) > tbody > tr:nth-child(9) > td:nth-child(2) > table > tbody > tr > td:nth-child(4)")[0].text.split("\xa0 ")[-1].strip()
        except:
          percent_lock_up = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(11) > tbody > tr:nth-child(9) > td:nth-child(2) > table > tbody > tr > td:nth-child(4)")[0].text.split("\xa0 ")[-1].strip()

        capital = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(3) > tbody > tr:nth-child(9) > td:nth-child(4)")[0].text.split("\xa0 ")[-1].strip()
        company_size = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(3) > tbody > tr:nth-child(4) > td:nth-child(4)")[0].text.split("\xa0 ")[-1].strip()

        time.sleep(1)
        driver.back()
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        profit = soup.select(f"body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(12) > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child({i}) > td:nth-child(8) > font")[0].text.split("\xa0 ")[-1].strip()
        time.sleep(1)


        if price_real == "-":
          pass
        else:
          headers=["name","market","sectors","price_hoping","price_real",
          "inv_comp","stock_amount","stock_fund","exec_company","listing_date","percent_newstock","percent_invest",
          "percent_personal","percent_lock_up","capital","company_size","profit"]
          data_dic[headers[0]] = name
          data_dic[headers[1]] = market
          data_dic[headers[2]] = sectors
          data_dic[headers[3]] = price_hoping
          data_dic[headers[4]] = price_real
          data_dic[headers[5]] = inv_comp
          data_dic[headers[6]] = stock_amount
          data_dic[headers[7]] = stock_fund
          data_dic[headers[8]] = exec_company
          data_dic[headers[9]] = listing_date
          data_dic[headers[10]] = percent_newstock
          data_dic[headers[11]] = percent_invest
          data_dic[headers[12]] = percent_personal
          data_dic[headers[13]] = percent_lock_up
          data_dic[headers[14]] = capital
          data_dic[headers[15]] = company_size
          data_dic[headers[16]] = profit

          total_lst.append(data_dic)

      except:
        pass


  total_df = pd.DataFrame(total_lst, columns=headers)

  return total_df.to_csv("./Data/total_to_db.csv")




def crawling_new():

  chrome_options = webdriver.ChromeOptions()
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

  page_num = [i for i in range(1,2)]
  new_lst = []

  for i in page_num:
    driver.get(f"http://www.38.co.kr/html/fund/index.htm?o=nw&page={i}")
    driver.maximize_window()
    time.sleep(1)
    print(new_lst)

    for i in range(1,21):
      data_dic = {}
      try:
        driver.find_element_by_css_selector(f"body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(12) > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child({i}) > td:nth-child(1) > a").click()
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        name = soup.select("b")[0].text
        market = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(3) > tbody > tr:nth-child(2) > td:nth-child(2)")[0].text.split("\xa0 ")[-1].strip()
        sectors = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(3) > tbody > tr:nth-child(3) > td:nth-child(2)")[0].text.split("\xa0 ")[-1].strip() 
        price_hoping = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(6) > tbody > tr:nth-child(3) > td:nth-child(2)")[0].text.split("\xa0 ")[-1].strip() 
        price_real = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(6) > tbody > tr:nth-child(4) > td:nth-child(2) > b")[0].text.split("\xa0 ")[-1].strip() 

        try:
          inv_comp = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(11) > tbody > tr:nth-child(9) > td:nth-child(2) > table > tbody > tr > td:nth-child(2)")[0].text.split("\xa0 ")[-1].strip()
        except:
          inv_comp = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(9) > tbody > tr:nth-child(9) > td:nth-child(2) > table > tbody > tr > td:nth-child(2)")[0].text.split("\xa0 ")[-1].strip()

        stock_amount = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(6) > tbody > tr:nth-child(1) > td:nth-child(2)")[0].text.split("\xa0 ")[-1].strip()
        stock_fund = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(6) > tbody > tr:nth-child(4) > td:nth-child(4)")[0].text.split("\xa0 ")[-1].strip() 
        exec_company = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(6) > tbody > tr:nth-child(5) > td:nth-child(2) > b")[0].text.split("\xa0 ")[-1].strip()

        try:
          listing_date = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(9) > tbody > tr:nth-child(10) > td:nth-child(2) > table > tbody > tr > td:nth-child(2)")[0].text.split("\xa0 ")[-1].strip()
        except:
          listing_date = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(11) > tbody > tr:nth-child(10) > td:nth-child(2) > table > tbody > tr > td:nth-child(2)")[0].text.split("\xa0 ")[-1].strip()

        percent_newstock = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(6) > tbody > tr:nth-child(2) > td:nth-child(2)")[0].text.split("\xa0 ")[-1].strip()
        try:
          percent_invest = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(9) > tbody > tr:nth-child(7) > td:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(2)")[0].text.split("\xa0")[2].strip()
          if percent_invest == "":
            percent_invest = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(9) > tbody > tr:nth-child(7) > td:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(2)")[0].text.split("\xa0")[1].strip().replace(" 주","")
        except:
          percent_invest = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(11) > tbody > tr:nth-child(7) > td:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(2)")[0].text.split("\xa0")[2].strip()
          if percent_invest == "":
            percent_invest = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(9) > tbody > tr:nth-child(7) > td:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(2)")[0].text.split("\xa0")[1].strip().replace(" 주","")

        try:
          percent_personal = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(9) > tbody > tr:nth-child(7) > td:nth-child(2) > table > tbody > tr:nth-child(5) > td:nth-child(2)")[0].text.split("\xa0")[2].strip()
          if percent_personal == "":
            percent_personal - soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(9) > tbody > tr:nth-child(7) > td:nth-child(2) > table > tbody > tr:nth-child(5) > td:nth-child(2)")[0].text.split("\xa0")[1].strip().replace(" 주","")
        except:
          percent_personal = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(11) > tbody > tr:nth-child(7) > td:nth-child(2) > table > tbody > tr:nth-child(5) > td:nth-child(2)")[0].text.split("\xa0")[2].strip()
          if percent_personal == "":
            percent_personal - soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(9) > tbody > tr:nth-child(7) > td:nth-child(2) > table > tbody > tr:nth-child(5) > td:nth-child(2)")[0].text.split("\xa0")[1].strip().replace(" 주","")
            
        try:
          percent_lock_up = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(9) > tbody > tr:nth-child(9) > td:nth-child(2) > table > tbody > tr > td:nth-child(4)")[0].text.split("\xa0 ")[-1].strip()
        except:
          percent_lock_up = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(11) > tbody > tr:nth-child(9) > td:nth-child(2) > table > tbody > tr > td:nth-child(4)")[0].text.split("\xa0 ")[-1].strip()

        capital = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(3) > tbody > tr:nth-child(9) > td:nth-child(4)")[0].text.split("\xa0 ")[-1].strip()
        company_size = soup.select("body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(3) > tbody > tr:nth-child(4) > td:nth-child(4)")[0].text.split("\xa0 ")[-1].strip()

        time.sleep(1)
        driver.back()
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        profit = soup.select(f"body > table:nth-child(9) > tbody > tr > td > table:nth-child(2) > tbody > tr > td:nth-child(1) > table:nth-child(12) > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child({i}) > td:nth-child(8) > font")[0].text.split("\xa0 ")[-1].strip()
        time.sleep(1)


        if price_real == "-":
          pass
        else:
          headers=["name","market","sectors","price_hoping","price_real",
          "inv_comp","stock_amount","stock_fund","exec_company","listing_date","percent_newstock","percent_invest",
          "percent_personal","percent_lock_up","capital","company_size","profit"]
          data_dic[headers[0]] = name
          data_dic[headers[1]] = market
          data_dic[headers[2]] = sectors
          data_dic[headers[3]] = price_hoping
          data_dic[headers[4]] = price_real
          data_dic[headers[5]] = inv_comp
          data_dic[headers[6]] = stock_amount
          data_dic[headers[7]] = stock_fund
          data_dic[headers[8]] = exec_company
          data_dic[headers[9]] = listing_date
          data_dic[headers[10]] = percent_newstock
          data_dic[headers[11]] = percent_invest
          data_dic[headers[12]] = percent_personal
          data_dic[headers[13]] = percent_lock_up
          data_dic[headers[14]] = capital
          data_dic[headers[15]] = company_size
          data_dic[headers[16]] = profit

          new_lst.append(data_dic)

      except:
        pass


  total_df = pd.DataFrame(new_lst, columns=headers)

  return total_df.to_csv("./Data/new_to_db.csv")
