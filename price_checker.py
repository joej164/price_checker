import requests
from bs4 import BeautifulSoup
import pytest


def find_playstation_price(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find_all(class_='price-display__price')[0].get_text()
    return price


def test_saga_scarlet_grace_price():
    url = 'https://store.playstation.com/en-us/product/UP0082-CUSA09653_00-SAGASCARLETHD001'
    expected_price = "$29.99"
    actual_price = find_playstation_price(url)
    assert expected_price == actual_price
