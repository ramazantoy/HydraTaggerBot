import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

from TelegramGroupManager import TelegramGroupManager

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.WARNING
)

Token = "5510219301:AAH5Z8-23KTXX6BAZS2z0ZCAy2ZIOgKaEzg"


async def startHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatID = update.effective_chat.id
    if (update.message.chat.type == "private"):
        await context.bot.send_message(chatID, text="Beni grubunuza yönetici olarak ekleyip kullanabilirsiniz.",
                                       parse_mode="HTML", reply_to_message_id=update.message.id)


async def utagHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):

        await update_handler(update, context)
        chatID = update.effective_chat.id

        print(update.message.text)
        if (update.message.chat.type == "private"):
            await context.bot.send_message(chatID, text="Beni grubunuza yönetici olarak ekleyip kullanabilirsiniz.",
                                           parse_mode="HTML", reply_to_message_id=update.message.id)
        else:

            currentGroup = telegramGroupManager.get_group(chatID)
            if (currentGroup is not None):
                await currentGroup.UserTagging(update=update,context=context)

async def update_handler(update, context):
    if (update.message is not None):
        telegramGroupManager.add_group(update.message.chat_id)


if __name__ == "__main__":
    ##auto-py-to-exe
    print("Hydra Tagger v2.0 Leon Version")
    telegramGroupManager = TelegramGroupManager()
    application = ApplicationBuilder().token(Token).build()
    utag_handler = CommandHandler('utag', utagHandler)
    start_handler = CommandHandler('start', startHandler)
    # Start the Bot
    application.add_handler(utag_handler)
    application.add_handler(start_handler)
    application.add_handler(MessageHandler(filters.ALL, update_handler))
    application.run_polling()
