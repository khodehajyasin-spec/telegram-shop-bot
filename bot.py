from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8986265488:AAHcWKvwMxba1XsDX16wjm4UXntvJPV37LQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام 👋\n"
        "ربات با موفقیت اجرا شد."
    )

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot Started...")
    app.run_polling()

if name == "main":
    main()
