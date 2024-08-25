import telebot
import requests

# Replace with your actual API tokens
TELEGRAM_BOT_TOKEN = '6513294858:AAHoS4Fb5Lxy9Bj-TfVqGLHqAwpdikbvi2w'
OPENWEATHERMAP_API_KEY = 'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}'

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(content_types=['location'])
def handle_location(message):
    location = message.location
    lat, lon = location.latitude, location.longitude

    # Call OpenWeatherMap API
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHERMAP_API_KEY}'
    response = requests.get(url)
    data = response.json()

    # Extract relevant weather info
    temp_kelvin = data['main']['temp']
    temp_celsius = temp_kelvin - 273.15
    weather_description = data['weather'][0]['description']

    # Respond to user
    bot.reply_to(message, f"Current weather: {temp_celsius:.1f}°C, {weather_description}")

bot.polling()
