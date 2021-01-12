# @rebootstr

import time
from Utils.MyVKLib import vk


def run():
    global params
    params = dict()
    vk.LongPoll.update_keys()
    while True:
        print(time.ctime())
        update = vk.LongPoll.get_update()
        for obj in update['updates']:
            if obj[0] == 4:  # new message
                print(update)
                input()


if __name__ == "__main__":
    run()

