#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Group 2  Amazon 

# 1  arti More
# 2  Utkarsha Chavan
# 3  Nanita Naryan
# 4  Shreya Trigune 
# 5  meera Sonawane
# 6  Chinmay Pathak
# 7  veer Jadhav
# 8  rutvika Vishwakarma
# 9  Mansi Ingle
# 10 Om Dabade

# # Problem Statement : Scrape The Data From Amazon. Save the product info in csv files. 
# You will create one csv file for Amazon and one for Myntra. Sort the data in descending order based on Price. 
# Later concatenate the data showing top 5 products from both CSV files into final CSV File.

# Column Names :  productName  productPrice  productDesc  productImg  productBuyLink


# In[4]:


import requests
import selenium 
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas  as pd
import time
import warnings 
warnings.filterwarnings('ignore')

#get the url
def get_url(product):
    product = product.replace(' ','+') 
    temple ="https://www.amazon.com/s?k={}"
    url = temple.format(product)
    return url


def get_product(card):
   
    # fetching the product name
    try:
        product_name = card.find('h2','a-size-mini a-spacing-none a-color-base s-line-clamp-4').text
    except:
        product_name ="not mentioned "
       
       
    # fetching the product_price
    try:
        product_price = card.find('span','a-offscreen').text
       
    except:
        product_price ="not mentioned "
      
        
    # fetching the product_desc
    try:
        productDesc = card.find('div','a-row a-size-base').text
        
    except:
        productDesc ="not mentioned "
       
       
    # fetching the product_img
    try:
        product_img = card.find('img','s-image')
        product_img =  product_img['src']
       
    except:
        product_img ="not mentioned "
        
       
    # fetching the product_buy
    try:
        product_buy = card.find('a','a-link-normal s-no-outline')
        product_buy = 'https://amazon.com'+ product_buy['href']
     
    except:
        product_buy ="not mentioned "
        
    all=(product_name,product_price,productDesc,product_img,product_buy)
    return all


# In[2]:


def main():
    record =[]
#     ur= input("enter the product name:")
    url= get_url('nike shoes')

        #
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(10)
    #creating beutifull soup object
    soup = BeautifulSoup(driver.page_source,'html.parser')
    cards = soup.find_all('div','sg-col-4-of-24 sg-col-4-of-12 s-result-item s-asin sg-col-4-of-16 sg-col s-widget-spacing-small sg-col-4-of-20')
   
    for everycard in cards:
        product = get_product(everycard)
        record.append(product)
    #here we using pandas  dataframe to save product in csv file
    
    col =['product_name','product_price','productDesc','product_img','product_buy']
    
    product_data = pd.DataFrame(record,columns=col)
    product_data.to_csv('D:\\intership\\amazon_product_data.csv',encoding ='utf-8')
    
        


# In[5]:


main()


# In[ ]:




