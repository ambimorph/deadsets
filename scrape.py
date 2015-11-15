from bs4 import BeautifulSoup
import requests
import os.path

url = 'https://www.cs.cmu.edu/~./gdead/setlists.html'
r = requests.get(url)
data = r.text
soup = BeautifulSoup(data)
prefix = 'https://www.cs.cmu.edu/~./gdead/'
yearpages = [link.get('href') for link in soup.find_all('a') if link.startswith('19')]
yearpages = [prefix + link.get('href') for link in soup.find_all('a') if link.string.startswith('19')]
showlist = []
for url in yearpages:
    soup = BeautifulSoup(requests.get(url).text)
    for link in soup.find_all('a'):
        showlist.append(link.get('href'))
for url in [prefix + sl for sl in showlist]:
    data = requests.get(url).text
    f = open(os.path.basename(url), 'w')
    f.write(data)
