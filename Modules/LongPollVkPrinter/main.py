import time
from Utils.MyVKLib import vk


def update_keys(mode=''):
    global params
    print("Обновляю ключи")
    data = vk.post("messages.getLongPollServer").json()['response']
    data['wait'] = 85
    params = data
    if mode == 'update':
        return get_update()


def get_update():
    global params
    print("Поиск обновлений")
    r = vk.get(
        "https://{server}?act=a_check&key={key}&ts={ts}&wait={wait}&mode=2version=3".format(server=params['server'],
                                                                                            key=params['key'],
                                                                                            wait=params['wait'],
                                                                                            ts=params['ts']),
        timeout=90).json()
    if 'failed' in r.keys():
        r = update_keys(mode='update')
    params['ts'] = r['ts']
    print("Обновлено")
    return r


def run():
    global params
    params = dict()
    update_keys()
    while True:
        print(time.ctime())
        update = get_update()
        for obj in update['updates']:
            if obj[0] == 4:  # new message
                print(update)
                input()


if __name__ == "__main__":
    run()

