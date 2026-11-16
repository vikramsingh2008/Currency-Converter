# Currency Converter Project

rates = {
    "INR": 1,
    "USD": 83,
    "EUR": 90,
    "GBP": 105
}

def convert_to_inr(amount, currency):

    result = amount * rates[currency]

    return result


def convert_currency(amount, from_currency, to_currency):

    inr_amount = convert_to_inr(amount, from_currency)

    result = inr_amount / rates[to_currency]

    return round(result, 2)



print("===== CURRENCY CONVERTER =====")
print("Available currencies: INR, USD, EUR, GBP")

amount_input = input("Enter amount: ")

try:
    amount = float(amount_input)

    if amount < 0:
        print("Amount cannot be negative.")

    else:
        from_currency = input("From currency: ").strip().upper()
        to_currency = input("To currency: ").strip().upper()

    
        if from_currency not in rates:
            print("Unsupported currency '" + from_currency +
                  "'. Available: INR, USD, EUR, GBP")

        elif to_currency not in rates:
            print("Unsupported currency '" + to_currency +
                  "'. Available: INR, USD, EUR, GBP")

        else:
            result = convert_currency(
                amount, from_currency, to_currency
            )

            print(f"{amount:g} {from_currency} = {result:.2f} {to_currency}")

except ValueError:
    print("Invalid amount. Enter a number.")
