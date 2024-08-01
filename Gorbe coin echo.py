from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

Token: Final = '6513294858:AAHoS4Fb5Lxy9Bj-TfVqGLHqAwpdikbvi2w'
Bot_user_name: Final = '@Gorbe_Coin_bot'


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('wellcome this gorbe coin پاره شدم تا همین بیاد')
def handle_response(text: str) ->str:
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

if __name__ == '__main__' :
    print('start polling')
    app = Application.builder().token(Token).build()
    app.add_handler(CommandHandler('start',start_command))
    #app.add_handler(CommandHandler('echo', echo))
    app.run_polling(poll_interval=1)