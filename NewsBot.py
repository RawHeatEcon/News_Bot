#Final_Project
#Rohit_Kumar

#CNN_Newsbot_with_HFT_Algorithm

#Packages
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from datetime import datetime

#Data Scraper
URL = 'https://www.cnn.com/business'
page = requests.get(URL)
raw_code = page.content
source = BeautifulSoup(raw_code, "html.parser")
headlines = source.find_all('span', class_='cd__headline-text')


#Stock Indexes
Stocks = ["Tesla","Apple","Trump","Walmart","3M", "Google"]
SP_500 = ["A","AAL","INTL","NVDA","GOOGL","3M"]

#Word Lists
positive = ["a","the","and"]
negative = ["if","Trump","no"]

#Algorithm Multipliers
SP_500_multiplier = 0
positive_multiplier = 0
negative_multiplier = 0

#Loop controllers
a = False
b = False
c = False


#Introduction
print("HERE ARE TODAY'S HEADLINES:","\n")
print("___________________________________________________________________________________")
print("\n")

for headline in headlines:
    print(headline.text)


#Headline scraper
#def timer():
#    def cnn():
#        for headline in headlines:
#            if headline != headline:
#                
#                print(headline.text)
#                print("\n")
#                print("\n")
#                print("\n")
#
#        time.sleep(interval)
#while True:
#    timer()
#
#timer()
#print("Execute the following orders:")

#def NewsBot():
#    headline_strength = 0
#    negative_multiplier = 0
#    positive_multiplier = 0
#    SP_500_multiplier = 0
#    for x in Stocks:
#        for headline in headlines:
#            if x in headline.text:
#                for y in positive:
#                    if y in headline.text:
#                        positive_multiplier = headline.text.count(y)
#                for z in negative:
#                    if z in headline.text:
#                        negative_multiplier = headline.text.count(z)
#                    headline_strength = (positive_multiplier + negative_multiplier)
#                algo = (SP_500_multiplier*10)*((headline_strength)*20)
#                if algo < 0:
#                    print("Sell", algo ," of", x,"shares.")
#                if algo > 0:
#                    print("Buy", algo ," of", x,"shares.")
#                else:
#                    print("Hold position for", x, ".")
#                SP_500_multiplier += 15
#   
#         
#    #Timestamp
#    def timestamp():
#        now = datetime.now()
#        date_time = now.strftime("%H:%M:%S %m/%d/%Y")
#        print("Accessed: ",date_time)
#
#    timestamp()
#    a == True

#NewsBot() 




#Index Checker
#def index():
#    for w in SP_500:
#        for headline in headlines:
#            if w in headline.text:
#                SP_500_multiplier2 += 1
#            else:
#                SP_500_multiplier2 = 0

#print("The S&P multiplier is: ",SP_500_multiplier)
#print("The positive multiplier is: ",positive_multiplier)
#print("The negative multiplier is: ",negative_multiplier)


#SP_500_multiplier2 = 0