import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from config import Token
from handlers import startHandler, utagHandler, cancelHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.WARNING
)

logger = logging.getLogger(__name__)


def main():
    print("@hydratagger")
    application = ApplicationBuilder().token(Token).build()

    application.add_handler(CommandHandler('start', startHandler))
    application.add_handler(CommandHandler('utag', utagHandler))
    application.add_handler(CommandHandler('cancel', cancelHandler))

    application.run_polling()


if __name__ == "__main__":
    main()