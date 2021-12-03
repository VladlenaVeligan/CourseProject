from typing import ValuesView
from bs4 import BeautifulSoup
import requests 

def parse(your_URL):
    HEADERS = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
	}
    
    s = requests.Session()

    response = s.get(your_URL, headers = HEADERS) 
    soup = BeautifulSoup(response.content, 'html.parser')
    values = soup.find('div', attrs={'class' : 'birzha_info_head_rates'})
    values = values.get_text().strip()

    birzha_time = soup.find('td', attrs={'class' : 'birzha_time'}) 
    birzha_time = birzha_time.get_text().strip().replace('Время последнего обновления', '')  
 
    return 'Курс биткоина на время ' + birzha_time + ' составляет ' + values

print(parse('https://myfin.by/crypto-rates/bitcoin'))