from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from flask import Flask
import threading
import os

TOKEN = "8918158673:AAHDQMvuwqS70MmMGknvlljQUf4DZ0F5dP4"
movies = {
    "test": {
        "title": "فیلم تست",
        "rating": "8/10",
        "genre": "ترسناک، روانشناختی",
        "description": "وقتی مرز بین واقعیت و کابوس از بین می‌رود...",
        "file_id": "BAACAgQAAxkBAAMFalLmAAHABPdKkwUf5Ecb52zufLakAAL_HgAC3niYUk8-BZSOitwCPAQ"
    }
}
app_web = Flask(__name__)

@app_web.route("/")
def home():
    return "Bot is running!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app_web.run(host="0.0.0.0", port=port)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    movie_key = context.args[0] if context.args else None

    if movie_key in movies:
        movie = movies[movie_key]

        await update.message.reply_text(
            f"🎬 {movie['title']}\n\n"
            f"⭐ امتیاز: {movie['rating']}\n"
            f"🎭 ژانر: {movie['genre']}\n\n"
            f"📝 {movie['description']}\n\n"
            "🎥 در حال ارسال فیلم..."
        )

        await update.message.reply_video(
            video=movie["file_id"]
        )

    else:
        await update.message.reply_text(
            "🎬 لطفاً از لینک اختصاصی فیلم استفاده کن."
        )

async def get_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = update.message.video
    await update.message.reply_text(f"File ID:\n{video.file_id}")

def run_bot():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.VIDEO, get_video))

    app.run_polling()

threading.Thread(target=run_web).start()
run_bot()