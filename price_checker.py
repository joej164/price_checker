import requests
from bs4 import BeautifulSoup
import pytest
import time


def find_playstation_price(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find(class_='psw-h3').text
    return price


def find_apple_store_price(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find_all(
        class_='inline-list__item inline-list__item--bulleted app-header__list__item--price')[0].get_text()
    return price


def find_pioneer_firmware_versions(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    all_rows = soup.find_all('tr')
    my_data = [row.text for row in all_rows if row.attrs.get(
        'data-model') == 'DMH-W4600NEX']

    output_list = []
    for row in my_data:
        output_list.extend(row.split())
    return output_list


def find_wacom_price(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find(class_='price').text
    return price


class Common:
    def setup(self):
        pass

    def teardown(self):
        time.sleep(5)   # Sleep for 5 seconds


class TestPlaystation(Common):
    def test_ps_castle_crashers_remastered(self):
        url = 'https://store.playstation.com/en-us/product/UP2015-CUSA14409_00-CASTLECRASHERSNA'
        expected_price = "$14.99"
        actual_price = find_playstation_price(url)
        assert expected_price == actual_price


class TestPioneer(Common):
    def test_pioneer_software_download_updated_firmware(self):
        url = 'https://www.pioneerelectronics.com/PUSA/Support/Downloads'
        expected_firmware = '1.3'
        dmh_4600_next_fw = find_pioneer_firmware_versions(url)
        assert expected_firmware in dmh_4600_next_fw
