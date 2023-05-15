from telegram import Update
class TelegramGroup:
    def __init__(self, chat_id):
        self.chat_id = chat_id

    def starthandler(self, update: Update, context):
        if update.message.chat.type == "private":
            context.bot.send_message(chat_id=self.chat_id,
                                     text="Beni grubunuza yönetici olarak ekleyip kullanabilirsiniz.",
                                     parse_mode="HTML",
                                     reply_to_message_id=update.message.id)


