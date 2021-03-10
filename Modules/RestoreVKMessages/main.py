# @rebootstr

from Utils.MyVKLib import vk

MODULE_CUSTOM_NAME = "Восстановление локально удаленных сообщений"
ORDER = 2

def getMessageId():
    r = vk.Rest.post("messages.getConversations", offset=0, count=1, filter="all", v="5.122").json()
    return r["response"]["items"][0]["conversation"]["last_message_id"]


def tryRestoreMessage(message_id):
    r = vk.Rest.post("messages.restore", message_id=message_id, v="5.122").json()
    if "error" in r.keys():
        return False
    else:
        return True


def run():
    print("How Many Message To restore?")
    count = int(input())
    message_id = getMessageId()
    message_id += count + 3
    while True:
        print(message_id, end="")
        if tryRestoreMessage(message_id):
            print(" Success")
            count -= 1
        else:
            print(" False")
        if count == 0:
            break
        message_id -= 1
    print("Thx for using program from RebootSTR :)")


if __name__ == "__main__":
    run()