# 🔮 Telegram Horoscope Bot

A simple Telegram bot that delivers daily horoscopes to users based on their zodiac sign and selected day (today, tomorrow, yesterday, or a specific date). Built with Python, Telebot (pyTelegramBotAPI), and deployed for on [Render](https://render.com) to keep the bot alive.

---

## 🚀 Features

- `/start` or `/hello` - greet the bot
- `/horoscope` — start the horoscope flow:

  - Select your **zodiac sign**
  - Choose a **day**: `today`, `tomorrow`, `yesterday`, or a custom date like `2025-05-20`
  - Real horoscopes via API for supported dates; default messages for custom dates

- Echoes any non-command messages for testing
- Runs 24/7 on Render using Flask + long polling

---

## 📲 How to Use the Bot

1. Open Telegram and search for [@rm_horoscope_bot](https://t.me/rm_horoscope_bot)
2. Type `/start` or `/hello` to begin
3. Type `/horoscope` to get a horoscope
4. Follow the prompts:
   - Select your zodiac sign (e.g. Leo, Aries)
   - Choose a day (`today`, `tomorrow`, `yesterday`, or a full date)
5. Get your daily prediction instantly 🌟

---

## ⚙️ Tech Stack

- Python
- Flask (to keep Render port alive)
- Deployed on [Render](https://render.com)

---
