import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
from timeit import default_timer as timer
from tqdm import tqdm
import random

# baselink = 'https://www.klenmarket.ru'
start = timer()

data = []
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36'}

with open("urlsAll.txt", "r") as file:
    linkList = file.readlines()
    # sleep(1)

for link in tqdm(linkList):
    r = requests.get(link.strip(), headers=headers, allow_redirects=False)
    sleep(random.randint(1, 5))
    if r.status_code != 200:
        continue
    # sleep(1)
    soup = BeautifulSoup(r.text, 'lxml')

    try:
        category1 = soup.findAll('a', class_='breadcrumbs__link')[1].text.strip().split(',')
    except:
        category1 = 'None'.split(',')
    try:
        category2 = soup.findAll('a', class_='breadcrumbs__link')[2].text.strip().split(',')
    except:
        category2 = 'None'.split(',')
    try:
        category3 = soup.findAll('a', class_='breadcrumbs__link')[3].text.strip().split(',')
    except:
        category3 = 'None'.split(',')
    try:
        category4 = soup.findAll('a', class_='breadcrumbs__link')[4].text.strip().split(',')
    except:
        category4 = 'None'.split(',')
    try:
        name = soup.find('h1').text.strip().split(',')
    except:
        name = 'None'.split(',')
    try:
        price = soup.find('span', class_='price__current-value').get('content')
    except:
        price = 'None'
    # try:
    #     code = soup.find('span', class_='origin__article').find('span', class_='text-warning').text.strip()
    # except:
    #     code = 'None'
    try:
        manufacturer = soup.find('div', class_='origin').find('a').text.strip()
    except:
        manufacturer = 'None'
    try:
        country = soup.find('span', class_='origin__country').text.strip()
    except:
        country = 'None'
    # link = 'https://stopgame.ru' + game.find('div', class_='caption').find('a').get('href')
    # score = items.find('div', class_='value').text
    # genre = items.find('div', class_='game-specs').findAll('div', class_='game-spec')[1].find('a').text
    data.append([' '.join(category1),
                 ' '.join(category2),
                 ' '.join(category3),
                 ' '.join(category4),
                 ' '.join(name),
                 price,
                 manufacturer,
                 country,
                 link.strip()])

# print(data)

#записываем полученные данные в CSV
header = ['category1',
          'category2',
          'category3',
          'category4',
          'name',
          'price',
          'manufacturer',
          'country',
          'link']
df = pd.DataFrame(data, columns=header)
df.to_csv(f'C:\\Users\d.novikov\PycharmProjects\Scrapers\Klenmarket.csv',sep=';', encoding='cp1251', errors='ignore')

end = timer()
print(end - start)
