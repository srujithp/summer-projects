from bs4 import BeautifulSoup
import requests
import pandas as pd


url = 'https://www.flipkart.com/search?' \
      'q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
page = requests.get(url)

# print(page.text)
soup = BeautifulSoup(page.text, 'html.parser')
print(soup.title)
name = []
price = []
rating = []
# class name is same for same type ex. name for different items
# name : _3wU53n price : _1vC4OE _2rQ-NK rating : hGSR34 all : _31qSD5

for a in soup.findAll('a', href=True, attrs={'class':'_31qSD5'}):
    name1 = a.find('div', attrs={'class':'_3wU53n'})
    price1 = a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    rating1 = a.find('div', attrs={'class':'hGSR34'})
    name.append(name1.text)
    price.append(price1.text)
    rating.append(rating1.text)

df = pd.DataFrame(list(zip(name, price, rating)))
df.columns = ['Model Name', 'Price', 'Rating']

print(df)
