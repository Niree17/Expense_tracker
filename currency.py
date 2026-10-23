import requests

API_URL = "https://api.frankfurter.dev/v2/rate"


def get_rate(from_currency:str="INR", to_currency:str="USD")-> float:
    url = f"{API_URL}/{from_currency.lower()}/{to_currency.lower()}"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    data = response.json()
    return data["rate"]


if __name__ == "__main__":
    print("1 INR in USD:", get_rate())