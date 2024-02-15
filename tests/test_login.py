import pytest
from selenium import webdriver


class TestLogin:
    def test_login(self):
        browser = webdriver.Chrome()
        browser.get('https://automatetheboringstuff.com')
