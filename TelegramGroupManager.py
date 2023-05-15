from TelegramGroup import TelegramGroup


class TelegramGroupManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.groups = []

        return cls._instance

    def add_group(self, chat_id: object) -> object:
        for group in self.groups:
            if group.chat_id == chat_id:
                print(f"Bu id zaten var. id : {chat_id}")
                return
        new_group = TelegramGroup(chat_id)
        self.groups.append(new_group)
        print(f"Id Başarıyla eklendi: {chat_id}")

    def print_groups(self):
        for group in self.groups:
            print("Group ID:", group.chat_id)

    def get_group(self, chat_id):
        for group in self.groups:
            if chat_id in group.chat_id:
                return group
        return None

