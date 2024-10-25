from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

from Handlers.handlers import startHandler, uTagHandler, cancelHandler, eTagHandler, fTagHandler, buttonHandler, \
    helpHandler, erosHandler, horoscopeHandler
from config import Token


def main():
    print("@hydratagger")
    application = ApplicationBuilder().token(Token).build()

    application.add_handler(CommandHandler('start', startHandler))
    application.add_handler(CommandHandler('utag', uTagHandler))
    application.add_handler(CommandHandler('cancel', cancelHandler))
    application.add_handler(CommandHandler('etag', eTagHandler))
    application.add_handler(CommandHandler('ftag', fTagHandler))
    application.add_handler(CommandHandler('help', helpHandler))
    application.add_handler(CommandHandler('eros', erosHandler))
    application.add_handler(CommandHandler('burc', horoscopeHandler))
    #application.add_handler(CommandHandler('slap', slapHandler))
    application.add_handler(CallbackQueryHandler(buttonHandler))

    application.run_polling()


if __name__ == "__main__":
    main()
