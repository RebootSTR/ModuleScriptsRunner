import requests
import hashlib

token = ""
httpToken = ""
httpSecret = ""


def post(method, **kwargs):
    if 'v' not in kwargs.keys():
        kwargs["v"] = "5.126"
    if 'access_token' not in kwargs.keys():
        kwargs["access_token"] = token
    kwargs["lang"] = "ru"
    kwargs["https"] = 1

    url = "https://api.vk.com/method/" + method + '?'
    for key, value in kwargs.items():
        url += f"{key}={value}&"
    url = url[:-1]
    try:
        r = requests.post(url)
    except:
        print('ошибка ')
        input()
    return r


def get(url, timeout):
    while True:
        try:
            r = requests.post(url, timeout=timeout)
            break
        except Exception:
            print('ошибка get запроса')
    return r


class http:

    @staticmethod
    def post(method, secret=httpSecret, **kwargs):
        if 'v' not in kwargs.keys():
            kwargs["v"] = 5.74
        if 'access_token' not in kwargs.keys():
            kwargs["access_token"] = httpToken
        kwargs["lang"] = "ru"
        kwargs["https"] = 1

        url = "https://api.vk.com/method/" + method + '?'
        for key, value in kwargs.items():
            url += f"{key}={value}&"
        url = url[:-1]
        sig = hashlib.md5((url[18:] + secret).encode("utf-8")).hexdigest()
        try:
            r = requests.post(url + "&sig={}".format(sig))
        except:
            print('ошибка ')
            input()
        return r
