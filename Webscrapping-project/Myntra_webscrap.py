#!/usr/bin/env python
# coding: utf-8

# In[61]:


import requests
import selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time
import warnings
warnings.filterwarnings('ignore')


# In[62]:


#get the url
def get_url(product):
    product = product.replace(' ','%20') 
    template ="https://www.myntra.com/{}"
    url = template.format(product)
    return url


# In[63]:


url = get_url('nike shoes')
print(url)


# In[68]:


def get_product(card):
   
    # fetching the product name
    try:
        product_name = card.find('h3','product-brand').text
    except:
        product_name ="not mentioned "
       
       
    # fetching the product_price
    try:
        product_price = card.find('span','product-strike').text
       
    except:
        product_price ="not mentioned "
      
        
    # fetching the product_desc
    try:
        productDesc = card.find('h4','product-product').text
        
    except:
        productDesc ="not mentioned "
       
       
    # fetching the product_img
    try:
        product_img = card.find('img','img-responsive')
        product_img =  product_img['src']
       
    except:
        product_img ="not mentioned "
        
       
    # fetching the product_buy
    try:
        product_buy = card.find('a')
        product_buy = 'https://www.myntra.com/'+ product_buy['href']
     
    except:
        product_buy ="not mentioned "
        
    all=(product_name,product_price,productDesc,product_img,product_buy)
    return all


# In[69]:


def main():
    record =[]
#url= input("enter the product name:")
    url= get_url('nike shoes')

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    try:
        driver.get(url)
        time.sleep(10)
        # creating beautiful soup object
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        cards = soup.find_all('li', class_=['product-base'])

        for everycard in cards:
            product = get_product(everycard)
            record.append(product)
    finally:
        driver.quit()
    #here we using pandas  dataframe to save product in csv file
    
    col =['product_name','product_price','productDesc','product_img','product_buy']
    
    product_data = pd.DataFrame(record,columns=col)
    product_data.to_csv('D:\\Myntra_scrap.csv',encoding ='utf-8')
main()


# In[ ]:




