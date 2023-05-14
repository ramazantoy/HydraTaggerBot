import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telethon import TelegramClient
import numpy as np
import time

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

accountID =12444421 
accountHash = '7afd603f843d2b40fa8617622e6a9d77'
Token = "5890782941:AAEgr72Cv1cbQrcwAh3Bl24rIiRnSSOWQk0"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    global Client
    
    async with  TelegramClient('session_name', accountID, accountHash) as Client:
        
        chatID = update.effective_chat.id
        userName   = update.effective_user.first_name
        userID   = update.effective_user.id
        command, *args = update.message.text.split()
        admin_warning = "Bu komutu sadece yöneticiler kullanabilir."

        args_warning = "<b>Kullanıcıları</b> çağırırken onlara bir mesajın olmasına ne dersin? 🤔\n<b>Örnek komut:</b> /utag Merhabalar\n\nveya istediğiniz mesaja /utag komutunu yanıtlayın"

        effective_user = await context.bot.getChatMember(chatID,userID)
        if str(effective_user.status) != "creator" and str(effective_user.status) != "administrator":
            await context.bot.send_message(chatID,text=admin_warning,parse_mode="HTML",reply_to_message_id=update.message.id)
        else:
            if len(context.args) != 0:
                userMention = f"<a href='tg://user?id={userID}'>{userName}</a>"
                starting_message = f"""
                    Etiket İşlemi {userMention} Tarafından Başlatıldı.\nİyi Sohbetler.
                """

                await context.bot.send_message(chatID,starting_message,parse_mode="HTML")

                members = await getChatMembers(chatID)
                botCounter = 0
                for x in members:
                    chatmember = await context.bot.get_chat_member(chatID,x[0])
                    if chatmember.user.is_bot:
                        members.remove(x)
                        botCounter += 1
                print(members)
                text=' '.join(args)
                text= f"<b>{text}</b>\n"
                header = f"\n{text}"
               
                arr = np.array(members)
                subarrays = np.array_split(arr,len(members)/5)
                for _members in subarrays:

                    message = f"{header}"
                    for index,_member in enumerate(_members):
                       message += f"<a href='tg://user?id={_member[0]}'>{_member[1]}</a>, "
                    await context.bot.send_message(chat_id=update.effective_chat.id, text=message,parse_mode="HTML")
                    time.sleep(3.5)
                print("bitti")
                finalMessage = f"✅ <b>İşlem Bitti !</b>\n\n👥 Etiketlenen Kullanıcı sayısı : {len(members)}\n🗣 Etiket işlemini başlatan : {userMention}"

                await context.bot.send_message(chatID,text=finalMessage,parse_mode="HTML")
            else:
                await context.bot.send_message(chatID,text=args_warning,parse_mode="HTML",reply_to_message_id=update.message.id)
async def getChatMembers(chatID):
    
    Members = []
    async for user in Client.iter_participants(chatID):
        
            user = [user.id,user.first_name]
            Members.append(user)
    
    return Members


if __name__ == "__main__":

    application = ApplicationBuilder().token(Token).build()
    
    start_handler = CommandHandler('utag', start)
    application.add_handler(start_handler)
    application.run_polling()