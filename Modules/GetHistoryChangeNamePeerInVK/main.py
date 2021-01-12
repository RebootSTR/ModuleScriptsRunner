from Utils.MyVKLib import vk
import time


def run():
    i = 0
    while True:
        r = vk.post("messages.getHistory", peer_id=2000000083, count=200, offset=200*i)
        json = r.json()["response"]["items"]
        for line in json:
            # print(line)
            if "action" in line.keys():
                if line["action"]["type"] == "chat_title_update":
                    print(line["action"]["text"] + " " + time.ctime(line["date"]))

        i += 1
        print("next?")

        input()


if __name__ == '__main__':
    run()
