from telegram import Update, Bot
from telegram.ext import Updater, MessageHandler, filters

# Define your bot token
TOKEN = '6513294858:AAHoS4Fb5Lxy9Bj-TfVqGLHqAwpdikbvi2w'

# Initialize the bot instance
my_bot = Bot(token=TOKEN)

# Define the start command handler
def start(update: Update, context) -> None:
    update.message.reply_text('Welcome to your Telegram bot!')

# Define the echo handler
def echo(update: Update, context) -> None:
    update.message.reply_text(update.message.text)

def main() -> None:
    # Create the Updater with the bot instance
    updater = Updater(bot=my_bot, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the start command handler
    dispatcher.add_handler(MessageHandler(filters.command, start))

    # Register the echo handler for text messages
    dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM, or SIG