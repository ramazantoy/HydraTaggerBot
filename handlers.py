from telegram import Update
from telegram.ext import ContextTypes
from tagging import perform_tagging
import asyncio

tagging_status = {}

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
    args = command_text[1] if len(command_text) > 1 else ""

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

                cancel_message = f"❌ <b>Etiketleme işlemi {canceller_mention} tarafından iptal edildi.</b>"
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