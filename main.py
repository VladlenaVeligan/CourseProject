from bs4 import BeautifulSoup
import csv
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

    try:   
        with open('data.csv', 'a', newline='') as file:
            writer =  csv.writer(file)
            writer.writerow([birzha_time, values])
            return 'Operation completed successfully!'
    except:
        return 'Error!!!'


    
print(parse('https://myfin.by/crypto-rates/bitcoin'))