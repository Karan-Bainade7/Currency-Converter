import requests

def get_exchange_rate(from_currency, to_currency):
    # API to get the latest exchange rate
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    
    try:
        response = requests.get(url)
        data = response.json()
        rate = data['rates'][to_currency]
        return rate
    except Exception as e:
        print("Error fetching exchange rate:", e)
        return None

def convert_currency(amount, from_currency, to_currency):
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    
    if exchange_rate:
        converted_amount = amount * exchange_rate
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("Conversion failed. Please try again.")

if __name__ == "__main__":
    # Get input from user
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the base currency (e.g., USD, EUR, INR): ").upper()
    to_currency = input("Enter the target currency (e.g., USD, EUR, INR): ").upper()
    
    # Perform currency conversion
    convert_currency(amount, from_currency, to_currency)
