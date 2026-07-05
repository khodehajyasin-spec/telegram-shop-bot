from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 خوش آمدید.\n\n"
        "به زودی ربات فروش VPN آماده خواهد شد."
    )