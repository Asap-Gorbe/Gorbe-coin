from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests

Token = '6513294858:AAHoS4Fb5Lxy9Bj-TfVqGLHqAwpdikbvi2w'
token = Token
Bot_user_name = '@Gorbe_Coin_bot'

async def Weather(update, context):
    message = update.message
    latitude = message.location.latitude
    longitude = message.location.longitude
    print(f"Received location: Latitude {latitude}, Longitude {longitude}")


    weather_data = fetch_weather_data(latitude, longitude)
    if weather_data:
        temperature = weather_data.get("hourly", {}).get("temperature_2m", [])
        if temperature:
            await update.message.reply_text(f"Temperature at 2 meters above ground level: {temperature[0]}°C")
        else:
            await update.message.reply_text("No temperature data found.")
    else:
        await update.message.reply_text("Failed to retrieve weather data.")

def fetch_weather_data(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m&forecast_days=1"

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

app = Application.builder().token(token).build()
app.add_handler(MessageHandler(filters.LOCATION, Weather))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('بقیه همینم ندارن')

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hi!')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(update.message.text)

if __name__ == '__main__':
    print('We are on ...')
    app.run_polling(poll_interval=1)
