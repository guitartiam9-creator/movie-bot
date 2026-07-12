from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = http://t.me/HorrorVaultBot

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات فیلم آماده است 🎬")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()