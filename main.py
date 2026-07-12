from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask
import threading
import os

TOKEN = "8918158673:AAEtODhVr06C0jkeH3KtDTYj9vKPwrVa8k0"

app_web = Flask(__name__)

@app_web.route("/")
def home():
    return "Bot is running!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app_web.run(host="0.0.0.0", port=port)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات فیلم آماده است 🎬")

def run_bot():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

threading.Thread(target=run_web).start()
run_bot()