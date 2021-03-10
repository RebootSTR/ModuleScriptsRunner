# @rebootstr

# You can import all modules
from Utils.MyVKLib import vk

from datetime import datetime

# You can add custom name for you module
MODULE_CUSTOM_NAME = "Получить статистику сообщений по дням"


# logic for run your module (NEED!!!)
def run():
    dialog_id = int(input("dialog id >> "))
    count = int(input("messages count >> "))
    dates = []
    for i in range(count // 200):
        r = vk.Rest.post("messages.getHistory", peer_id=dialog_id, count=200, offset=200*i)
        for item in r.json()["response"]["items"]:
            dates.append(item["date"])
    if count % 200 != 0:
        r = vk.Rest.post("messages.getHistory", peer_id=dialog_id, count=count%200, offset=200 * (count // 200))
        for item in r.json()["response"]["items"]:
            dates.append(item["date"])
    printStatistic(dates)


def printStatistic(dates:list):
    statistic = {}
    for date in dates:
        key = datetime.utcfromtimestamp(date).strftime('%Y-%m-%d')
        if key in statistic.keys():
            statistic[key] += 1
        else:
            statistic[key] = 1
    print("Для анализа было выбрано " + str(len(dates)) + " сообщений")
    counter = 0
    for date, count in statistic.items():
        counter += 1
        if counter == len(statistic):
            break
        print(date + " -> " + str(count) + " сообщений")


# if you want run module without runner
if __name__ == '__main__':
    run()
