from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8918158673:AAH1zrfNMg5rfwqWjSLLm15s_7CBUIXO3Y8"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات فیلم آماده است 🎬")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()