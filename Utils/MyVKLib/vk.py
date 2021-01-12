# @rebootstr

import requests
import hashlib

try:
    from Utils.MyVKLib.settings import token
except:
    # Enter your token HERE
    token = ""


httpToken = ""
httpSecret = ""


class Rest:

    @staticmethod
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

    @staticmethod
    def get(url, timeout):
        while True:
            try:
                r = requests.post(url, timeout=timeout)
                break
            except Exception:
                print('ошибка get запроса')
        return r


class LongPoll:

    @staticmethod
    def update_keys(mode=''):
        global params
        print("Обновляю ключи")
        data = Rest.post("messages.getLongPollServer").json()['response']
        data['wait'] = 85
        params = data
        if mode == 'update':
            return LongPoll.get_update()

    @staticmethod
    def get_update():
        global params
        print("Поиск обновлений")
        r = Rest.get(
            "https://{server}?act=a_check&key={key}&ts={ts}&wait={wait}&mode=2version=3".format(server=params['server'],
                                                                                                key=params['key'],
                                                                                                wait=params['wait'],
                                                                                                ts=params['ts']),
            timeout=90).json()
        if 'failed' in r.keys():
            r = LongPoll.update_keys(mode='update')
        params['ts'] = r['ts']
        print("Обновлено")
        return r


class HttpRest:

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
