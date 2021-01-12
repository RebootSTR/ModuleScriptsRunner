# @rebootstr

from Utils.MyVKLib import vk


def run():
    dialogs = []

    r = vk.Rest.post("messages.getConversations", filter="all", count=100).json()
    conversations = r["response"]["items"]
    for item in conversations:
        conv = item["conversation"]
        peer = conv["peer"]
        if peer["type"] != "chat":
            continue
        dialogs.append({
            "id": peer["local_id"],
            "name": conv["chat_settings"]["title"]
        })

    for dialog in dialogs:
        print(f"{dialog['id']} - {dialog['name']}")
    print()