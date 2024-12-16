from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

def getting_webdriver_ready():
    chrome_path="D:\DownLoad\chromewww\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    chrome_webdriver=webdriver.ChromeService(executable_path=chrome_path)
    options=webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')                             
    options.add_argument('--disable-dev-shm-usage')
    wd=webdriver.Chrome(service=chrome_webdriver,options=options)
    return wd


def Search_for_and_in_amazon():
    search_item=input("Enter the Item you want to search for : ")
    wd=getting_webdriver_ready()
    url="https://www.amazon.eg"
    wd.get(url)
    
    element3=wd.find_element(By.ID,"twotabsearchtextbox")
    element3.clear()
    element3.send_keys(search_item)
    element3.submit()
    #time.sleep(45)
    return wd.page_source
    
    #element.find_element()
def finding_data():
    data=Search_for_and_in_amazon()
    soap=BeautifulSoup(data,"html.parser")
    print(soap.prettify())
    return soap

def converting_TO_CSV(list_items,ct):
   
   df=pd.DataFrame(list_items) 
   df.to_csv(f"D:\DownLoad\learining courses\DEPI-DS-AI\Projects\webscrapping\Project 2\data\items_data{ct}.csv")
   print('CSV file created successfully open data folder') 



def getting_data():
    ct=0
    Searchagain=True
    while(Searchagain):
        soap=finding_data()
    
        list_items=[]
        item_data=soap.find_all("div",class_="a-section a-spacing-base")
        for item in item_data:
            item_dict={}
            item_dict['name']=item.find("h2",class_="a-size-base-plus a-spacing-none a-color-base a-text-normal").text.strip()
            item_dict['NO.in Stock'] = item.find("span", class_="a-size-base a-color-price").text.strip()if item.find("span", class_="a-size-base a-color-price") else "N/A" 
            item_dict['price']=item.find("span", class_="a-price-whole").text.strip() if item.find("span", class_="a-price-whole") else "N\A"
            item_dict['Rating']=item.find("span", class_="a-icon-alt").text.strip() if item.find("span", class_="a-icon-alt") else "N\A"
            item_dict['No.Ratings']=item.find("span",class_="a-size-base s-underline-text").text.strip()if item.find("span", class_="a-size-base s-underline-text") else "N/A"
            list_items.append(item_dict)
        print(list_items)
        ct+=1
        converting_TO_CSV(list_items,ct)
        ask = input("Do you want to search for something else? [Y]/[N]: ").lower()
        while ask not in ["y", "n"]:
            ask = input("Please type [Y] or [N]: ").lower()
        
        Searchagain = ask == "y"
        
        


getting_data()

    
