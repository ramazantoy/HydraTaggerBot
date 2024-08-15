import asyncio
from telethon import TelegramClient
from config import accountID, accountHash, DebugId
from Utils.utils import clean_html
from Tag.tagtype import TagType
from Emoji.emoji import EmojiGenerator

client = TelegramClient('session', accountID, accountHash, device_model="Telegram Bot", system_version="1.0",
                        app_version="1.0", lang_code="en")
chunk_size = 5
emoji = EmojiGenerator()


async def send_error_message(context, error):
    error_message = f"Hata oluştu: {str(error)}"
    await context.bot.send_message(chat_id=DebugId, text=error_message)


async def perform_tagging(update, context, chatID, userID, userName, args, tagType):
    try:
        if not client.is_connected():
            await client.start()

        entity = await client.get_entity(chatID)
        members = []
        async for user in client.iter_participants(entity):
            if not user.bot and user.id != userID:
                members.append([user.id, user.first_name or "None"])

        if not members:
            await context.bot.send_message(chatID, "Etiketlenecek üye bulunamadı.", parse_mode="HTML")
            return

        text = clean_html(f"<b>{args}</b>\n")
        header = f"\n{text}"
        total_members = len(members)

        for i in range(0, total_members, chunk_size):
            chunk = members[i:i + chunk_size]
            message = f"{header}"
            for member in chunk:
                if tagType == TagType.NORMAL:
                    message += f"<a href='tg://user?id={member[0]}'>{member[1]}</a>, "
                elif (tagType == TagType.EMOJI):
                    message += f"<a href='tg://user?id={member[0]}'>{emoji.get_random_emoji()}</a>, "
                else:
                    message += f"<a href='tg://user?id={member[0]}'>{emoji.get_random_flag()}</a>, "

            success = False
            retries = 0
            while not success and retries < 3:
                try:
                    await context.bot.send_message(chat_id=chatID, text=message, parse_mode="HTML")
                    success = True
                except Exception as e:
                    retries += 1
                    wait_time = 2 ** retries
                    await asyncio.sleep(wait_time)

            if not success:
                await send_error_message(context, "Failed to send message after 3 retries")

            if i > 0:
                await asyncio.sleep(3)

        userMention = f"<a href='tg://user?id={userID}'>{userName}</a>"
        finalMessage = f"✅ <b>Etiketleme işlemi tamamlandı.</b>\n\n👥 Etiketlenen Kullanıcı sayısı : {len(members)}\n🗣 Etiket işlemini başlatan : {userMention}"
        await context.bot.send_message(chatID, text=finalMessage, parse_mode="HTML")

    except Exception as e:
        await context.bot.send_message(chatID,
                                       text=f"Etiketleme işlemi sırasında bir hata oluştu: {str(e)}\nLütfen botun yönetici olduğundan ve gerekli izinlere sahip olduğundan emin olun.",
                                       parse_mode="HTML")
        await send_error_message(context, e)
