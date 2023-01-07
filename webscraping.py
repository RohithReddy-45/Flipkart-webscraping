#Importing modules
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

#Scraping the data
URL= "https://www.flipkart.com/search?q=television"
r=requests.get(URL)

#checking status code
if r.status_code != 200:
    print("Error while fetching the page")
    exit()
else:
    content = r.content
soup = bs(content,'html.parser')

titles = soup.find_all('div',class_="_4rR01T")
prices = soup.find_all('div',class_="_30jeq3 _1_WHN1")
discount=soup.find_all('div',class_="_3Ay6Sb")
cus_rating=soup.find_all('div',class_="_3LWZlK")

ratngsrews = soup.find_all('span',class_="_34hpFu")
tvtitle=[]
tRatingsReviews=[]
tvprice=[]
discounts=[]
Cust_rating=[]

for title,tratrev,price,disc,cusrating in zip(titles,ratngsrews,prices,discount,cus_rating):
    tvtitle.append(title.text)
    tRatingsReviews.append(tratrev.text)
    tvprice.append(price.text)
    discounts.append(disc.text)
    Cust_rating.append(cusrating.text)
#saving the information in csv file
info={'TITLES' :tvtitle,'TOTAL RATINGS & REVIEWS' :tRatingsReviews,'PRICES':tvprice,'DISCOUNT':discounts,'CUSTRATING':Cust_rating}
df=pd.DataFrame(data=info)
df.to_csv("televisiondata.csv")