import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Your Telegram bot token (replace with your actual token)
TOKEN = '6513294858:AAHoS4Fb5Lxy9Bj-TfVqGLHqAwpdikbvi2w'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hi! I'm your echo bot. Send me any message, and I'll echo it back!")

def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main() -> None:
    updater = Updater(TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
