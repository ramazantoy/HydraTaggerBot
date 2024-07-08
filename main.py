import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telethon import TelegramClient
import numpy as np
import asyncio
from typing import Dict

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.WARNING
)



tagging_status: Dict[int, asyncio.Task] = {}

async def startHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatID = update.effective_chat.id
    if update.message.chat.type == "private":
        await context.bot.send_message(chatID, text="Beni grubunuza yönetici olarak ekleyip kullanabilirsiniz.",
                                       parse_mode="HTML", reply_to_message_id=update.message.message_id)

async def utagHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatID = update.effective_chat.id

    if update.message.chat.type == "private":
        await context.bot.send_message(chatID, text="Beni grubunuza yönetici olarak ekleyip kullanabilirsiniz.",
                                       parse_mode="HTML", reply_to_message_id=update.message.message_id)
        return

    userName = update.effective_user.first_name
    userID = update.effective_user.id
    command_text = update.message.text.strip().split(maxsplit=1)
    command = command_text[0] if command_text else ""
    args = command_text[1].split() if len(command_text) > 1 else []

    admin_warning = "Sadece yöneticiler tarafından kullanılabilir."
    args_warning = "<b>Beni</b> kullanmak için bir mesaj yazmalısın."

    effective_user = await context.bot.get_chat_member(chatID, userID)
    if str(effective_user.status) not in ["creator", "administrator"]:
        await context.bot.send_message(chatID, text=admin_warning, parse_mode="HTML",
                                       reply_to_message_id=update.message.message_id)
        return

    if chatID in tagging_status and not tagging_status[chatID].done():
        await context.bot.send_message(chatID,
                                       text="Şu anda başka bir etiketleme işlemi devam ediyor. Lütfen önce onu tamamlayın veya iptal edin.",
                                       parse_mode="HTML", reply_to_message_id=update.message.message_id)
        return

    if not args:
        await context.bot.send_message(chatID, text=args_warning, parse_mode="HTML",
                                       reply_to_message_id=update.message.message_id)
        return

    userMention = f"<a href='tg://user?id={userID}'>{userName}</a>"
    starting_message = f"Etiketleme işlemi {userMention} tarafından başlatılıyor....."

    await context.bot.send_message(chatID, starting_message, parse_mode="HTML",
                                   reply_to_message_id=update.message.message_id)

    tagging_task = asyncio.create_task(perform_tagging(update, context, chatID, userID, userName, args))
    tagging_status[chatID] = tagging_task

async def perform_tagging(update, context, chatID, userID, userName, args):
    async with TelegramClient('session_name', accountID, accountHash) as Client:
        members = []
        async for user in Client.iter_participants(chatID):
            if not user.bot:
                members.append([user.id, user.first_name])

    text = ' '.join(args)
    text = f"<b>{text}</b>\n"
    header = f"\n{text}"

    if len(members) > 10:
        arr = np.array(members)
        subarrays = np.array_split(arr, len(arr) // 5)
        for _members in subarrays:
            if chatID not in tagging_status or tagging_status[chatID].done():
                break
            message = f"{header}"
            for _member in _members:
                message += f"<a href='tg://user?id={_member[0]}'>{_member[1]}</a>, "
            await context.bot.send_message(chat_id=chatID, text=message, parse_mode="HTML")
            await asyncio.sleep(2)
    else:
        if chatID in tagging_status and not tagging_status[chatID].done():
            messageText = header
            for _member in members:
                messageText += f"<a href='tg://user?id={_member[0]}'>{_member[1]}</a>, "
            await context.bot.send_message(chat_id=chatID, text=messageText, parse_mode="HTML")

    userMention = f"<a href='tg://user?id={userID}'>{userName}</a>"
    if chatID in tagging_status and not tagging_status[chatID].done():
        finalMessage = f"✅ <b>Etiketleme işlemi tamamlandı.</b>\n\n👥 Etiketlenen Kullanıcı sayısı : {len(members)}\n🗣 Etiket işlemini başlatan : {userMention}"
    else:
        finalMessage = f"❌ <b>Etiketleme işlemi iptal edildi.</b>\n\n🗣 Etiket işlemini başlatan : {userMention}"

    await context.bot.send_message(chatID, text=finalMessage, parse_mode="HTML")
    if chatID in tagging_status:
        del tagging_status[chatID]


async def cancelHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatID = update.effective_chat.id
    if update.message.chat.type != "private":
        effective_user = await context.bot.get_chat_member(chatID, update.effective_user.id)
        if str(effective_user.status) in ["creator", "administrator"]:
            if chatID in tagging_status and not tagging_status[chatID].done():
                tagging_status[chatID].cancel()


                canceller_id = update.effective_user.id
                canceller_name = update.effective_user.first_name
                canceller_mention = f"<a href='tg://user?id={canceller_id}'>{canceller_name}</a>"

                cancel_message =  f"❌ <b>Etiketleme işlemi  {canceller_mention} tarafından iptal edildi.</b>"
                await context.bot.send_message(chatID, text=cancel_message, parse_mode="HTML",
                                               reply_to_message_id=update.message.message_id)
            else:
                await context.bot.send_message(chatID, text="Şu anda aktif bir etiketleme işlemi yok.",
                                               parse_mode="HTML", reply_to_message_id=update.message.message_id)
        else:
            await context.bot.send_message(chatID, text="Bu komutu sadece yöneticiler kullanabilir.", parse_mode="HTML",
                                           reply_to_message_id=update.message.message_id)
    else:
        await context.bot.send_message(chatID, text="Bu komut sadece gruplarda kullanılabilir.", parse_mode="HTML",
                                       reply_to_message_id=update.message.message_id)

if __name__ == "__main__":
    print("@hydratagger")
    application = ApplicationBuilder().token(Token).build()
    utag_handler = CommandHandler('utag', utagHandler)
    start_handler = CommandHandler('start', startHandler)
    cancel_handler = CommandHandler('cancel', cancelHandler)
    application.add_handler(utag_handler)
    application.add_handler(start_handler)
    application.add_handler(cancel_handler)
    application.run_polling()