

accountID = 12444421
accountHash = '7afd603f843d2b40fa8617622e6a9d77'
Token = "5510219301:AAH5Z8-23KTXX6BAZS2z0ZCAy2ZIOgKaEzg"

from telethon import TelegramClient


class TelegramClientManager:

    async def getChatMembers(self, chatID):
        Members = []

        global Client

        async with  TelegramClient('session_name', accountID, accountHash) as Client:
            async for user in Client.iter_participants(chatID):
                user = [user.id, user.first_name]
                Members.append(user)

        return Members