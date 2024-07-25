from horoscope import get_horoscope
import logging

logger = logging.getLogger(__name__)

async def perform_horoscoping(update,context, chatID, messageId, args):

    response = get_horoscope(args)

    if response is not None:
        await context.bot.send_message(chat_id=chatID, text=response, reply_to_message_id=messageId)
    else:
        await context.bot.send_message(chat_id=chatID, text="Burç yorumunuzu şu an getiremiyorum.\nLütfen daha sonra tekrar deneyiniz ya da komutu doğru girdiğinizden emin olun 😊🙏🪐🌎", reply_to_message_id=messageId)