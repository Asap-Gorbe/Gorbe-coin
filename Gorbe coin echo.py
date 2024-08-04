from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes,CallbackContext
Token: Final = '6513294858:AAHoS4Fb5Lxy9Bj-TfVqGLHqAwpdikbvi2w'

Bot_user_name: Final = '@Gorbe_Coin_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('بقیه همینم ندارن')


def main() -> None:
        updater = Updater(TOKEN)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", start))
        updater.start_polling()
        updater.idle()

if __name__ == '__main__' :
    print(' we are on ...')
    app = Application.builder().token(Token).build()
    app.add_handler(CommandHandler('start',start_command))
    app.run_polling(poll_interval=1)