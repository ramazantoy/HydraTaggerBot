import logging
from telegram.ext import ApplicationBuilder, CommandHandler,CallbackQueryHandler
from config import Token
from handlers import startHandler,uTagHandler, cancelHandler,eTagHandler,fTagHandler,buttonHandler,helpHandler,erosHandler,horoscopeHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.WARNING
)

logger = logging.getLogger(__name__)


def main():
    print("@hydratagger")
    application = ApplicationBuilder().token(Token).build()

    application.add_handler(CommandHandler('start', startHandler))
    application.add_handler(CommandHandler('utag', uTagHandler))
    application.add_handler(CommandHandler('cancel', cancelHandler))
    application.add_handler(CommandHandler('etag',eTagHandler))
    application.add_handler(CommandHandler('ftag',fTagHandler))
    application.add_handler(CommandHandler('help',helpHandler))
    application.add_handler(CommandHandler('eros',erosHandler))
    application.add_handler(CommandHandler('burc',horoscopeHandler))
    application.add_handler(CallbackQueryHandler(buttonHandler))
    application.run_polling()


if __name__ == "__main__":
    main()