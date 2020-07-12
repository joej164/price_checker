import requests
from bs4 import BeautifulSoup
import pytest
import time


def find_playstation_price(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find_all(class_='price-display__price')[0].get_text()
    return price


def find_apple_store_price(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find_all(
        class_='inline-list__item inline-list__item--bulleted app-header__list__item--price')[0].get_text()
    return price


class TestClass:
    def setup(self):
        pass

    def teardown(self):
        time.sleep(5)   # Sleep for 1 second

    def test_ps_saga_scarlet_grace_price(self):
        url = 'https://store.playstation.com/en-us/product/UP0082-CUSA09653_00-SAGASCARLETHD001'
        expected_price = "$29.99"
        actual_price = find_playstation_price(url)
        assert expected_price == actual_price

    def test_ps_castle_crashers_remastered(self):
        url = 'https://store.playstation.com/en-us/product/UP2015-CUSA14409_00-CASTLECRASHERSNA'
        expected_price = "$14.99"
        actual_price = find_playstation_price(url)
        assert expected_price == actual_price

    def test_ps_dungeons_3_complete_collection(self):
        url = 'https://store.playstation.com/en-us/product/UP2060-CUSA07824_00-0331006500115282'
        expected_price = "$39.99"
        actual_price = find_playstation_price(url)
        assert expected_price == actual_price

    def test_apple_saga_scarlet_grace_price(self):
        url = 'https://apps.apple.com/us/app/saga-scarlet-grace-ambitions/id1237502412'
        expected_price = "$29.99"
        actual_price = find_apple_store_price(url)
        assert expected_price == actual_price
