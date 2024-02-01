from bs4 import BeautifulSoup
import requests

URL = 'https://realpython.com/tutorials/community/'

response = requests.get(URL)
response_content = response.content

soup = BeautifulSoup(response_content, features='html.parser')

# <img src=---->
# images = soup.find_all('img', class_='card-img-top')

tags = soup.find_all('a', class_='badge badge-light text-muted')
tags = set(tags)
for t in tags:
    path = t['href']
    print(f'https://realpython.com{path}')