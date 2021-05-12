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
    price_str = soup.find(class_='version').text
    price_arr = price_str.split()
    price = price_arr[1]

    return price


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


class TestPioneer(Common):
    def test_pioneer_software_download_updated_firmware(self):
        url = 'https://www.pioneerelectronics.com/PUSA/Car/NEX/DMH-W4600NEX'
        expected_firmware = '1.31'
        dmh_4600_next_fw = find_pioneer_firmware_versions(url)
        assert expected_firmware in dmh_4600_next_fw
