from telegram.ext import ContextTypes
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from tagging import perform_tagging
from erosing import perform_eros
from tagtype import TagType
from horoscoping import  perform_horoscoping
import asyncio

tagging_status = {}

async  def helpHandler(update: Update,context : ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🐺 Hydra Duyuru Kanalı", url="https://t.me/kurtoyunn")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    chatID = update.effective_chat.id
    helpText = "Merhaba, komutlarım aşağıdaki gibididir.\n\n/utag - Normal etiketleme yapar.\n\n/etag - Emoji ile etiketleme yapar.\n\n/ftag - Bayrak ile etiketleme işlemi yapar.\n\n/cancel - Etiketleme işlemini iptal eder.\n\n/eros - Erosun okunu fırlatır.\n\n/burc - Günlük burç yorumunuzu yazar.\n\nBeni grubunuza yönetici olarak ekleyip kullanabilirsiniz.\n\nİyi Eğlenceler :)"
    await context.bot.send_message(
        chatID,
        text=helpText,
        parse_mode="HTML",
        reply_markup= reply_markup,
        reply_to_message_id=update.message.message_id
    )


async def horoscopeHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatID = update.effective_chat.id
    messageId = update.message.message_id

    command_text = update.message.text.strip().split(maxsplit=1)
    args = command_text[1] if len(command_text) > 1 else ""
    print(args)
    return await perform_horoscoping(update, context, chatID, messageId, args)
async def erosHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatID = update.effective_chat.id
    userID = update.effective_user.id
    return await perform_eros(update, context, chatID, userID)
async def uTagHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await tagHandler(update, context, TagType.NORMAL)

async def eTagHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await tagHandler(update, context, TagType.EMOJI)

async def fTagHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    return await tagHandler(update, context, TagType.FLAG)

async def startHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chatID = update.effective_chat.id
    if update.message.chat.type == "private":

        keyboard = [
            [InlineKeyboardButton("🐺 Hydra Duyuru Kanalı", url="https://t.me/kurtoyunn")],
            [InlineKeyboardButton("📚 Komutlarım", callback_data="commands")],
            [InlineKeyboardButton("🛠 Developer", url="https://t.me/leonbrave")],
            [InlineKeyboardButton("➕ Beni Grubuna Ekle", url=f"https://t.me/hydrataggerbot?startgroup=true")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await context.bot.send_message(
            chatID,
            text="Merhaba! 🫡 Ben Hydra Tagger, grubunuzdaki kullanıcıları etiketleyebilirim! 🎉\n\nBeni grubunuza yönetici olarak ekleyip kullanabilirsiniz. 🚀 Aşağıdaki butonları kullanarak daha fazla bilgi alabilirsiniz. 📚",
            parse_mode="HTML",
            reply_markup=reply_markup,
            reply_to_message_id=update.message.message_id
        )

async def buttonHandler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "commands":
        comamnd_list = """
Mevcut komutlar:
/utag - Normal etiketleme yapar.
/etag - Emoji ile etiketleme yapar.
/ftag - Bayrak ile etiketleme işlemi yapar.
/eros - Eros'un okunu fırlatır.
/burc - Günlük burç yorumunuzu yazar.
/cancel - Etiketleme işlemini iptal eder.

Komutları kullanmak için gruba yönetici olarak eklenmiş olmalıyım.
        """
        await query.edit_message_text(text=comamnd_list, parse_mode="HTML")

async def tagHandler(update: Update, context: ContextTypes.DEFAULT_TYPE,tagType):
    chatID = update.effective_chat.id

    if update.message.chat.type == "private":
        await context.bot.send_message(chatID, text="Beni grubunuza yönetici olarak ekleyip kullanabilirsiniz.",
                                       parse_mode="HTML", reply_to_message_id=update.message.message_id)
        return

    userName = update.effective_user.first_name
    userID = update.effective_user.id
    command_text = update.message.text.strip().split(maxsplit=1)
    args = command_text[1] if len(command_text) > 1 else ""

    admin_warning ="Sadece yöneticilerin kullanabileceği bir komut bu 😶\nLütfen yönetici yetkilerinizi kontrol edin. ⁉️"

    args_warning = "<b>Lütfen</b> gruba iletmek istediğin bir mesaj yazarak tekrar dene! 📢"

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

    if not args and tagType==TagType.NORMAL:
        await context.bot.send_message(chatID, text=args_warning, parse_mode="HTML",
                                       reply_to_message_id=update.message.message_id)
        return

    userMention = f"<a href='tg://user?id={userID}'>{userName}</a>"
    starting_message = f"Etiketleme işlemi {userMention} tarafından başlatıldı. 🔉🔊"

    await context.bot.send_message(chatID, starting_message, parse_mode="HTML",
                                   reply_to_message_id=update.message.message_id)



    tagging_task = asyncio.create_task(perform_tagging(update, context, chatID, userID, userName, args,tagType))
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
                await context.bot.send_message(chatID, text="Üzgünüm, şu anda bir etiketleme işlemi yapmıyorum. 🤷‍♂️",
                                               parse_mode="HTML", reply_to_message_id=update.message.message_id)
        else:
            await context.bot.send_message(chatID, text="Sadece yöneticilerin kullanabileceği bir komut bu! 😢 \n "
                                                        "Lütfen yönetici yetkilerinizi kontrol edin.",
                                           parse_mode="HTML",
                                           reply_to_message_id=update.message.message_id)
    else:
        await context.bot.send_message(chatID, text="Bu komut sadece gruplarda kullanılabilir. 😢", parse_mode="HTML",
                                       reply_to_message_id=update.message.message_id)