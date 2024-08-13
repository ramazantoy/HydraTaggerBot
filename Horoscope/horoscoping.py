from Horoscope.horoscope import get_horoscope
import logging
from config import DebugId


async def send_error_message(context, error):
    error_message = f"Hata oluştu: {str(error)}"
    await context.bot.send_message(chat_id=DebugId, text=error_message)

async def perform_horoscoping(update, context, chatID, messageId, args):
    try:
        response = get_horoscope(args)
        if response is not None:
            await context.bot.send_message(chat_id=chatID, text=response, reply_to_message_id=messageId)
        else:
            await context.bot.send_message(
                chat_id=chatID,
                text="Burç yorumunuzu şu an getiremiyorum.\nLütfen daha sonra tekrar deneyiniz ya da komutu doğru girdiğinizden emin olun 😊🙏🪐🌎",
                reply_to_message_id=messageId
            )
    except Exception as e:
        await context.bot.send_message(
            chat_id=chatID,
            text="Burç yorumu alınırken bir hata oluştu. Lütfen daha sonra tekrar deneyin.",
            reply_to_message_id=messageId
        )
        await send_error_message(context, e)