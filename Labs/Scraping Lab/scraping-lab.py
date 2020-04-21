# SCRAPING PROBLEMS
# Twitter Scraping (15pts)
# Go to your favorite follow on Twitter.  (not someone who posts explicit materials please)
# Inspect the twitter feed in Chrome.
# You'll notice that the tweets are stored in a ordered list <ol></ol>, and individual tweets are contained as list items <li></li>.
# Use BeautifulSoup and requests to grab the text contents of last 5 tweetslocated on the twitter page you chose.
# Print the tweets in a nicely formatted way.
# Have fun.  Again, nothing explicit.

#  print("{} {}!".format("Hello", "World"))
from bs4 import BeautifulSoup
import requests
import time
import urllib.request
import certifi
from selenium import webdriver

twit_url = "https://twitter.com/FWProbotics"
driver = webdriver.Chrome("/Users/starrothkopf/PycharmProjects/P2_SP20/Labs/Scraping Lab/chromedriver")
driver.implicitly_wait(10)
driver.get(twit_url)

last_height = driver.execute_script("return document.body.scrollHeight")
x = 0
pages_to_scroll = 20

while x < pages_to_scroll:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    x += 1
    time.sleep(1)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

soup = BeautifulSoup(driver.page_source, 'lxml')
print(soup.prettify())

title = soup.find("title")
print(title.text)

extra = soup.find_all(dir="auto")
for i in extra:
    print(i.text)
# not having luck figuring out how to target specific tweets



# Weather Scraping (15pts)
# Below is a link to a 10-day weather forecast at weather.com
# Pick the weather for a city that has the first letter as your name.
# Use requests and BeautifulSoup to scrape data from the weather table.
# Print a synopsis of the weather for the next 10 days.
# Include the day and date, description, high and low temp, chance of rain, and wind. (2pts each)
# Print the weather for each of the next 10 days to the user in a readable sentences.
# You can customize the text as you like, but it should be readable as a sentence without errors. (5pts)
# You will need to target specific classes or other attributes to pull some parts of the data.
# Sample sentence:
# Wednesday, April 4 will be Partly Cloudy/Windy with a High of 37 degrees and a low of 25, humidity at 52%.  There is 0% chance of rain with winds out of the WNW at 22 mph.
# if the sentence is a little different than shown, that will work; do what you can.  Don't forget about our friend string.format()



url = "https://weather.com/weather/tenday/l/69bedc6a5b6e977993fb3e5344e3c06d8bc36a1fb6754c3ddfb5310a3c6d6c87"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

title = soup.find("title") #
print(title.text)

days = soup.find_all(headers="day")
descriptions = soup.find_all(headers="description")
highlow = soup.find_all(headers="hi-lo")
rainchance = soup.find_all(headers="precip")
windspeed = soup.find_all(headers='wind')

for i in range(len(days)):
    print("\n", days[i].text,
          "will be", descriptions[i].text,
          "with a high and low of", highlow[i].text,
          "degrees. There will be a", rainchance[i].text,
          "chance of rain with winds of", windspeed[i].text, ".")
