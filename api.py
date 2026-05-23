import requests
import config

def get_crypto_data(coin):
    url = f'{config.BASE_URL}/coins/{coin}'

    try:
        response = requests.get(url)
        
        if response.status_code != 200:
            print(f'Error fetching data for {coin}. Status code: {response.status_code}')
            return None
        
        return response.json()
    
    except requests.exceptions.RequestException:
        return None