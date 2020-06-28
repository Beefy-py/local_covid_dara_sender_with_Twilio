import time
import requests
from bs4 import BeautifulSoup

url = requests.get('https://www.worldometers.info/coronavirus/country/suriname/').text
url_for_population = requests.get("https://www.worldometers.info/world-population/population-by-country/").text

soup = BeautifulSoup(url, 'html.parser')
soup_pop = BeautifulSoup(url_for_population, 'html.parser')

population = int(soup_pop.find('tbody').find('a', href='/world-population/suriname-population/'). \
                 parent.parent.find('td', style="font-weight: bold;").text.replace(',', ""))
all_info_scraped = soup.find_all('div', id="maincounter-wrap")

all_data = {}

for i in all_info_scraped:
    header = i.find('h1').text
    counter = i.find('span').text
    all_data[header] = int(counter)
all_data['Active Cases:'] = all_data['Coronavirus Cases:'] - all_data['Recovered:']

percentage_active_cases = f"{round((all_data['Active Cases:'] / population) * 100, 4)}%"
percentage_total_cases = f"{round((all_data['Coronavirus Cases:'] / population) * 100, 4)}%"
