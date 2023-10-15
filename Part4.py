from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

from selenium.webdriver.chrome.service import Service

service = Service(executable_path='D:\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


Description = []  # List to store description of the product
Price = []  # List to store price of the product
Rating = []  # List to store rating of the product
Review = []  # List to store reviews of the product
Size = []  # List to store size of the product
Discount = []  # List to store Discount on the product
Previous_Price = []  # List to store the price before discount

driver.get("https://www.flipkart.com/gaming-laptops-store?otracker=nmenu_sub_Electronics_0_Gaming%20Laptops&otracker=nmenu_sub_E")
content = driver.page_source
soup = BeautifulSoup(content,features="html.parser")
# print(soup)
for a in soup.findAll('div',attrs={'class':'_37K3-p'}):
 print (a)
 description = a.find('a', attrs={'class': 's1Q9rs'})
  Description.append(description.text)

  price = a.find('div', attrs={'class': '_30jeq3'})
  Price.append(price.text)

  if (a.find('div', attrs={'class': '_3LWZlK'})):
   rating = a.find('div', attrs={'class': '_3LWZlK'}).text
   Rating.append(rating)
  else:
   rating = "No rating available"
   Rating.append(rating)

  if (a.find('span', attrs={'class': '_2_R_DZ'})):
   review = a.find('span', attrs={'class': '_2_R_DZ'}).text
   Review.append(review)
  else:
   review = "No review available"
   Review.append(review)

  if (a.find('div', attrs={'class': '_3Djpdu'})):
   size = a.find('div', attrs={'class': '_3Djpdu'}).text
   Size.append(size)
  else:
   size = "No size available"
   Size.append(size)

  if (a.find('div', attrs={'class': '_3Ay6Sb'})):
   discount = a.find('div', attrs={'class': '_3Ay6Sb'}).text
   Discount.append(discount)
  else:
   discount = "No discount available"
   Discount.append(discount)

  if (a.find('div', attrs={'class': '_3I9_wc'})):
   previous_price = a.find('div', attrs={'class': '_3I9_wc'}).text
   Previous_Price.append(previous_price)
  else:
   previous_price = "No previous price available"
   Previous_Price.append(previous_price)


 # name=a.find('a', attrs={'class':'s1Q9rs'})
 # price=a.find('div',attrs={'class':'_30jeq3'})
 # rating=a.find('div',attrs={'class':'_3LWZlK'})
 # if name:
 #  products.append(name.text)
 # else:
 #  print("No product")
 # if price:
 #  prices.append(price.text)
 # else:
 #  print("No price")
 # if rating:
 #  ratings.append(rating.text)
 # else:
 #  print("no ratings")
 df = pd.DataFrame({'Description': Description, 'Price': Price, 'Rating': Rating, 'Review': Review, 'Size': Size, 'Discount': Discount,
  'Price Before Discount': Previous_Price})
 df.to_csv('products.csv', index=False, encoding='utf-8')
# from selenium import webdriver
# from bs4 import BeautifulSoup
# from selenium.webdriver.chrome.options import Options
# import pandas as pd
# from selenium.webdriver.chrome.service import Service
#
# service = Service(executable_path='D:\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe')
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)
#
# chrome_options = Options()
# prefs = {"profile.managed_default_content_settings.images": 2}
# chrome_options.add_experimental_option("prefs", prefs)
# # driver = webdriver.Chrome(executable_path=r'D:\\Downloads\\chromedriver-win64 (1)\\chromedriver-win64\\chromedriver.exe',
# #                           options=chrome_options)
#
# Description = []  # List to store description of the product
# Price = []  # List to store price of the product
# Rating = []  # List to store rating of the product
# Review = []  # List to store reviews of the product
# Size = []  # List to store size of the product
# Discount = []  # List to store Discount on the product
# Previous_Price = []  # List to store the price before discount
#
# # Loop For Multiple Pages
# for page in range(1, 9661):
#
#  driver.get(
#   "https://www.flipkart.com/search?q=all+laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page=" + str(
#    page))
#  content = driver.page_source
#  soup = BeautifulSoup(content)
#  print(soup)
#  main = soup.findAll('div', attrs={'class': '_4ddWXP'})
#  for a in soup.findAll('div', attrs={'class': '_4ddWXP'}):
#   print(a)
#
#   description = a.find('a', attrs={'class': 's1Q9rs'})
#   Description.append(description.text)
#
#   price = a.find('div', attrs={'class': '_30jeq3'})
#   Price.append(price.text)
#
#   if (a.find('div', attrs={'class': '_3LWZlK'})):
#    rating = a.find('div', attrs={'class': '_3LWZlK'}).text
#    Rating.append(rating)
#   else:
#    rating = "No rating available"
#    Rating.append(rating)
#
#   if (a.find('span', attrs={'class': '_2_R_DZ'})):
#    review = a.find('span', attrs={'class': '_2_R_DZ'}).text
#    Review.append(review)
#   else:
#    review = "No review available"
#    Review.append(review)
#
#   if (a.find('div', attrs={'class': '_3Djpdu'})):
#    size = a.find('div', attrs={'class': '_3Djpdu'}).text
#    Size.append(size)
#   else:
#    size = "No size available"
#    Size.append(size)
#
#   if (a.find('div', attrs={'class': '_3Ay6Sb'})):
#    discount = a.find('div', attrs={'class': '_3Ay6Sb'}).text
#    Discount.append(discount)
#   else:
#    discount = "No discount available"
#    Discount.append(discount)
#
#   if (a.find('div', attrs={'class': '_3I9_wc'})):
#    previous_price = a.find('div', attrs={'class': '_3I9_wc'}).text
#    Previous_Price.append(previous_price)
#   else:
#    previous_price = "No previous price available"
#    Previous_Price.append(previous_price)
#
# df = pd.DataFrame(
#  {'Description': Description, 'Price': Price, 'Rating': Rating, 'Review': Review, 'Size': Size, 'Discount': Discount,
#   'Price Before Discount': Previous_Price})
# df.to_csv('products.csv', index=False, encoding='utf-8')
# driver.close()