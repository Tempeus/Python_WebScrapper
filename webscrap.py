import requests
from bs4 import BeautifulSoup

# Define the URL of the website you want to scrape
url = "https://www.example.com"

# Use requests to get the contents of the website
page = requests.get(url)

# Use BeautifulSoup to parse the page
soup = BeautifulSoup(page.content, 'html.parser')

# Find all the elements on the page with the class "article-title"
titles = soup.find_all(class_="article-title")

# Loop through the elements and print the text of each one
for title in titles:
    print(title.text)
