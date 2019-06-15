import unittest
import requests


def test_google():
    assert requests.get(url="https://google.com").status_code == 200
