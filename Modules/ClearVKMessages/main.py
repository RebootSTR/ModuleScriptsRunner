import random
import time
from Utils.MyVKLib import vk


def run():
    id = 100
    tmp = input("peer id: ")
    if tmp != "":
        id = int(tmp)
    while True:
        MY_ID = 189104642
        exit = False
        # ожидание команды
        while True:
            print("zapros")
            r = vk.post("messages.getHistory", count=5, peer_id=2000000000 + id)
            for item in r.json()["response"]["items"]:
                if item["text"] == "/delete" and item["from_id"] == MY_ID:
                    if len(item['fwd_messages']) > 0:
                        date = item['fwd_messages'][0]['date']
                    else:
                        date = item['reply_message']['date']
                    exit = True
                    break
            if exit:
                break
            time.sleep(5)
        # поиск админов
        admins = []
        r = vk.post("messages.getConversationMembers", peer_id=2000000000 + id)
        for item in r.json()['response']['items']:
            if item['member_id'] != MY_ID and "is_admin" in item.keys():
                admins.append(item['member_id'])

        print(admins)
        # сбор ИД сообщений
        r = vk.post("messages.getHistory", count=50, peer_id=2000000000 + id)
        ids = []
        for item in r.json()['response']['items']:
            if item['date'] >= date:
                if "action" not in item.keys():
                    if item['from_id'] not in admins:
                        ids.append(item['id'])
            else:
                break
        # Удаление
        print("deleting")
        r = vk.post("messages.delete", message_ids=ids.__str__()[1:-1], delete_for_all=1)
        print(r.text)
        # отчет об удалении
        r = vk.post("messages.send", chat_id=id, message=f"Уничтожено {len(ids) - 1} сообщений(я) :)",
                 random_id=random.randint(10000000, 99999999))
        time.sleep(5)
        # удаление отчета
        r = vk.post("messages.delete", message_ids=r.json()['response'], delete_for_all=1)
        # break # <-- Убрать цикличность


if __name__ == "__main__":
    run()