from Slap.slapGenerator import SlapGenerator
from Slap.slapGenerator import ResultGenerator


slapGenerator=SlapGenerator()
resultGenerator=ResultGenerator()


async def perform_slaping(update, context, chatID, slapperId, slapToId):
    slapMessage = slapGenerator.getRandomSlapMessage()
    slapResult = resultGenerator.getRandomResult()

    slapper = update.effective_user
    slapTo = update.message.reply_to_message.from_user

    slapper_mention = f'<a href="tg://user?id={slapperId}"><b>{slapper.first_name}</b></a>'
    slapTo_mention = f'<a href="tg://user?id={slapToId}"><b>{slapTo.first_name}</b></a>'

    message = f"<b>{slapper_mention}, {slapTo_mention}'ın {slapMessage}.\n\n{slapResult}.</b>"

    await context.bot.send_message(chat_id=chatID, text=message, parse_mode='HTML')