from eros import ErosGenerator
import random
from tagging import client
import logging


logger = logging.getLogger(__name__)
eros=ErosGenerator()

async def perform_eros(update, context, chatID, userID):
    try:
        if not client.is_connected():
            await client.start()

        entity = await client.get_entity(chatID)
        members = []
        async for user in client.iter_participants(entity):
            if not user.bot and user.id != userID:
                members.append([user.id, user.first_name or "None"])

        if len(members) < 2:
            await context.bot.send_message(chatID, "Eros için yeterli üye bulunamadı.", parse_mode="HTML")
            return

        selected_members = random.sample(members, 2)
        compatibility = random.randint(0, 100)

        message = "💘 Erosun oku atıldı! 🏹\n\n"
        message += f"<a href='tg://user?id={selected_members[0][0]}'>{selected_members[0][1]}</a> 💕 "
        message += f"<a href='tg://user?id={selected_members[1][0]}'>{selected_members[1][1]}</a>\n\n"
        message += f"{eros.get_random_message(compatibility)}\n\n"
        message += f"❤️ İlişki uyumu: %{compatibility}"


        try:
            await context.bot.send_message(chat_id=chatID, text=message, parse_mode="HTML")
        except Exception as e:
            logger.error(f"Error sending Eros message: {e}")
            await context.bot.send_message(chatID,
                                           text="Eros mesajı gönderilirken bir hata oluştu. Lütfen daha sonra tekrar deneyin.",
                                           parse_mode="HTML")
            return

    except Exception as e:
        logger.error(f"Error in perform_eros: {e}")
        await context.bot.send_message(chatID,
                                       text=f"Eros işlemi sırasında bir hata oluştu: {str(e)}\nLütfen botun yönetici olduğundan ve gerekli izinlere sahip olduğundan emin olun.",
                                       parse_mode="HTML")