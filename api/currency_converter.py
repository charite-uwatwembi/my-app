
import requests

def convert_currency(amount, from_currency, to_currency):
    base_url = "https://api.exchangerate-api.com/v4/latest/{}".format(from_currency)

    response = requests.get(base_url)
    data = response.json()

    if response.status_code == 200:
        if to_currency in data["rates"]:
            exchange_rate = data["rates"][to_currency]
            converted_amount = amount * exchange_rate
            return converted_amount
        else:
            return "Invalid currency code"
    else:
        return "Error fetching exchange rates"

def main():
    print("Welcome to the Currency Converter!")
    print("We Help You Convert Currencies!")

    amount = float(input("Enter the amount to convert: "))
    print("Please enter the currency in capital letters!")
    from_currency = input("Enter the currency to convert from: ")
    to_currency = input("Enter the currency to convert to: ")

    converted_amount = convert_currency(amount, from_currency, to_currency)
    if isinstance(converted_amount, float):
        print(f"The converted amount is: {converted_amount:.2f} {to_currency}")
    else:
        print(converted_amount)

if __name__ == "__main__":
    main()

