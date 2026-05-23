from colorama import Fore, Style
def show_crypto(data):
    name = data['name']
    symbol = data['symbol'].upper()

    price = data['market_data']['current_price']['usd']
    market_cap = data['market_data']['market_cap']['usd']
    change_24h = data['market_data']['price_change_percentage_24h']
    ranking = data['market_cap_rank']


    print("\n"+ '=' * 40)
    print(f"{name} ({symbol})")
    print('=' * 40)

    print(f"{'Price':15}: ${price:,.2f}")
    print(f"{'Market Cap':15}: ${market_cap:,.0f}")
    if change_24h >= 0:
        color = Fore.GREEN
    else:
        color = Fore.RED
    sign = '+' if change_24h >= 0 else ""
    print(f"{'24h change':15}: {color}{sign}{change_24h:.2f}%{Style.RESET_ALL}")
    print(f"{'Ranking':15}: #{ranking}")

    print('=' * 40)