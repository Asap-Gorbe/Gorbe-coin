from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

Token = '6513294858:AAHoS4Fb5Lxy9Bj-TfVqGLHqAwpdikbvi2w'
Bot_user_name = '@Gorbe_Coin_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('بقیه همینم ندارن')

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi!')


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

    def main() -> None:
        updater = Updater(TOKEN)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(CommandHandler('Hello', Hello))
        updater.start_polling()
        updater.idle()


if __name__ == '__main__':
    print(' we are on ...')
    app = Application.builder().token(Token).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('Hello', hello_command))
    app.add_handler(CommandHandler('echo', echo))

    app.run_polling(poll_interval=1)