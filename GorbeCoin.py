from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

Token = '6513294858:AAHoS4Fb5Lxy9Bj-TfVqGLHqAwpdikbvi2w'
token = Token
Bot_user_name = '@Gorbe_Coin_bot'

async def Location(update, context):
    message = update.message
    latitude = message.location.latitude
    longitude = message.location.longitude
    print(f"Received location: Latitude {latitude}, Longitude {longitude}")
    await update.message.reply_text(f"your location Latitude: {latitude}, Longitude: {longitude}")

app = Application.builder().token(token).build()
app.add_handler(MessageHandler(filters.LOCATION, Location))


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('بقیه همینم ندارن')

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi!')


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)



if __name__ == '__main__':
    if __name__ == '__main__':
        print(' we are on ...')
        app.run_polling(poll_interval=1)