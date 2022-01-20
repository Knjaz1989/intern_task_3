import requests
from bs4 import BeautifulSoup


response = requests.get('https://www.python.org/')
soup = BeautifulSoup(response.text, 'html.parser')

anonces = soup.find('div', class_="shrubbery")
print("Upcoming Events")

for anonce in anonces.find_all('li'):
    print(anonce.text)
