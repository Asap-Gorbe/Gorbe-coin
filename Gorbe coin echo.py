from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
Token: Final = '6513294858:AAHoS4Fb5Lxy9Bj-TfVqGLHqAwpdikbvi2w'
Bot_user_name: Final = '@Gorbe_Coin_bot'
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('wellcome this gorbe coin پاره شدم تا همین بیاد')
def handle_response(text: str) ->str:
    proccesd_text :str = text.lower()
    if 'hello' in proccesd_text:
        return ('Hey!!')
    else:
        return (str(text))

    async def Command_Handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
        message_type: str = update.message.chat.type

    import logging
    from telegram import Update
    from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
    def main() -> None:
        updater = Updater(TOKEN)

        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

        updater.start_polling()
        updater.idle()
if __name__ == '__main__' :
    print(' we are on mother fucker')
    app = Application.builder().token(Token).build()
    app.add_handler(CommandHandler('start',start_command))
    #app.add_handler(CommandHandler('echo', echo))
    app.run_polling(poll_interval=1)
