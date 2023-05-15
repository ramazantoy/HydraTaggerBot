from telegram import Update
from telegram.ext import ContextTypes
import numpy as np
import time
from TelegramClientManager import TelegramClientManager


class TelegramGroup:


    def __init__(self, chat_id):
        self.chat_id = chat_id


    async def UserTagging(self,update: Update, context: ContextTypes.DEFAULT_TYPE):

        print("Telegram Group Object")
        print(update.effective_chat.id)
        print(update.effective_user.first_name)
        chatID = update.effective_chat.id
        userName = update.effective_user.first_name
        userID = update.effective_user.id
        command, *args = update.message.text.split()
        admin_warning = "Sadece yöneticiler tarafından kullanılabilirim.)."

        args_warning = "<b>Beni</b> kullanmak için bir mesaj yazmalısın.)"

        effective_user = await context.bot.getChatMember(chatID, userID)
        if str(effective_user.status) != "creator" and str(effective_user.status) != "administrator":
            await context.bot.send_message(chatID, text=admin_warning, parse_mode="HTML",
                                           reply_to_message_id=update.message.id)
        else:
            if len(context.args) != 0:
                userMention = f"<a href='tg://user?id={userID}'>{userName}</a>"
                starting_message = f"""
                                                             Etiketleme  işlemi {userMention}  tarafından başlatılıyor.....
                                                         """

                await context.bot.send_message(chatID, starting_message, parse_mode="HTML",
                                               reply_to_message_id=update.message.id)

                manager=TelegramClientManager()
                members = await manager.getChatMembers(chatID=chatID)
                membersTemp = members.copy()
                for x in membersTemp:
                    chatmember = await context.bot.get_chat_member(chatID, x[0])
                    if chatmember.user.is_bot:
                        members.remove(x)

                text = ' '.join(args)
                text = f"<b>{text}</b>\n"
                header = f"\n{text}"

                if len(members) > 10:
                    arr = np.array(members)
                    subarrays = np.array_split(arr, len(arr) / 5)
                    for _members in subarrays:
                        message = f"{header}"
                        for index, _member in enumerate(_members):
                            message += f"<a href='tg://user?id={_member[0]}'>{_member[1]}</a>, "
                        await context.bot.send_message(chat_id=update.effective_chat.id, text=message,
                                                       parse_mode="HTML")
                       #time.sleep(3.5)
                else:
                    messageText = ""
                    for _member in members:
                        messageText += f"<a href='tg://user?id={_member[0]}'>{_member[1]}</a>, "

                await context.bot.send_message(chat_id=update.effective_chat.id, text=messageText,
                                               parse_mode="HTML")
                finalMessage = f"✅ <b>Etiketleme işlemi tamamlandı.</b>\n\n👥 Etiketlenen Kullanıcı sayısı : {len(members)}\n🗣 Etiket işlemini başlatan : {userMention}"
                await context.bot.send_message(chatID, text=finalMessage, parse_mode="HTML",
                                               reply_to_message_id=update.message.id)


            else:
                await context.bot.send_message(chatID, text=args_warning, parse_mode="HTML",
                                               reply_to_message_id=update.message.id)


