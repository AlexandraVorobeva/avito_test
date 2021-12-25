import requests
import lxml
from bs4 import BeautifulSoup


def get_currency(currency_id: str):
    """Fetch exchange rate for ruble."""
    page = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    src = page.text
    soup = BeautifulSoup(src, "lxml")
    exchange_rate = soup.find(id=currency_id).find_next("value").get_text()
    return round(float(exchange_rate.replace(",", ".")), 2)


USD = get_currency("R01235")
EUR = get_currency("R01239")
CNY = get_currency("R01375")
