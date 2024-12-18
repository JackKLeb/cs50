import requests
import sys

try:
    n = sys.argv[1]
except IndexError:
    print("Missing command-line arguement")

try:
    n = float(n)
except ValueError:
    print("Command-line arguemnt is not a number")

try:
    pull = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    result = pull.json()
    price = result["bpi"]["USD"]["rate_float"]
    total = n * price
    print(f"${total:,.4f}")

except requests.RequestException:
    pass
