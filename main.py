from display import show_crypto
from api import get_crypto_data

    
def main():
    print("Welcome to the Crypto Tracker!")

    while True:
        coins = input("\nEnter Cryptocurrency separated by commas (exit to quit): ").strip().lower()

        if coins == "exit":
            print("Exiting the program.")
            return
        
        for coin in coins.split(','):
            coin = coin.strip()
            if not coin:
                print("No cryptocurrency entered.")
                continue
            
            data = get_crypto_data(coin)
            if data:
                show_crypto(data)
            else:
                print(f"{coin.capitalize()} not found, Please check the name and try again.")

if __name__ == "__main__":
    main()