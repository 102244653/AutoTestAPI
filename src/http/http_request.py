import requests


def auto_get(url):
    res = requests.get(url)
    return res.status_code, res.json()


def auto_post(url, **param):
    pass