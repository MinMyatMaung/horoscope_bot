import os
import threading
from dotenv import load_dotenv
from flask import Flask
import telebot
from utils import get_daily_horoscope

# Load environment variables from .env
load_dotenv()

# Read BOT_TOKEN from environment
BOT_TOKEN = os.environ.get('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is not set. Check your .env file!")

bot = telebot.TeleBot(BOT_TOKEN)

# --- Telegram Bot Handlers ---

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['horoscope'])
def sign_handler(message):
    text = (
        "What's your zodiac sign?\n"
        "Choose one: *Aries*, *Taurus*, *Gemini*, *Cancer*, *Leo*, *Virgo*, "
        "*Libra*, *Scorpio*, *Sagittarius*, *Capricorn*, *Aquarius*, and *Pisces*."
    )
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, day_handler)

def day_handler(message):
    sign = message.text.strip().capitalize()
    text = (
        "What day do you want to know?\n"
        "Choose one: *TODAY*, *TOMORROW*, *YESTERDAY*, or a date like `2025-04-24`."
    )
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, fetch_horoscope, sign)

def fetch_horoscope(message, sign):
    day = message.text.strip().lower()
    horoscope = get_daily_horoscope(sign, day)
    data = horoscope["data"]
    horoscope_message = (
        f'*Horoscope:* {data["horoscope_data"]}\n'
        f'*Sign:* {sign}\n'
        f'*Day:* {data["date"]}'
    )
    bot.send_message(message.chat.id, "Here's your horoscope!")
    bot.send_message(message.chat.id, horoscope_message, parse_mode="Markdown")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

# --- Flask App to Keep Render Service Alive ---

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

# --- Run both Telegram bot and Flask app ---

def run_telegram_bot():
    bot.infinity_polling()

if __name__ == '__main__':
    # Start the bot in a separate thread
    threading.Thread(target=run_telegram_bot).start()
    
    # Start Flask app on Render-required port
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
