# https://www.256kilobytes.com/content/show/2001/an-introduction-to-scraping-with-python-and-beautifulsoup
import urllib.request
from bs4 import BeautifulSoup

url = "https://www.imdb.com/title/tt1477834/" # Aquaman

response = urllib.request.urlopen(url)
html = response.read() # this is what you would see if you downloaded a website with wget

soup = BeautifulSoup(html, 'html.parser') # parse the html

title = soup.h1.find(text=True, recursive=False)
rating = soup.find("span", itemprop="ratingValue")
characters =  soup.select("td.character")

print("The movie "+title+"got a rating of "+str(rating.text)+" from IMDB users.")

print("This is a list of the main characters:")
for character in characters:
    print(character.text.strip())
