from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = " 8986265488:AAGXzIrE1giyjYWICplY944qbaryAD_ntSM "

CARD_NUMBER = "6219861831024566"
CARD_OWNER = "احمد محمودی"
ADMIN_USERNAME = "@config_admin_starlink"
SHOP_NAME = "V2ray Shop"

keyboard = [
    ["🛒 خرید سرویس", "📦 سرویس‌های من"],
    ["💳 شماره کارت", "☎️ پشتیبانی"],
]

reply_markup = ReplyKeyboardMarkup(
    keyboard,
    resize_keyboard=True
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"👋 به {SHOP_NAME} خوش آمدید.",
        reply_markup=reply_markup,
    )


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "🛒 خرید سرویس":
        await update.message.reply_text(
            "🔹 پلن ۱ ماهه\n"
            "🔹 پلن ۳ ماهه\n"
            "🔹 پلن ۶ ماهه\n\n"
            "به‌زودی این بخش به پنل مرزبان متصل می‌شود."
        )

    elif text == "📦 سرویس‌های من":
        await update.message.reply_text("هنوز سرویسی برای شما ثبت نشده است.")

    elif text == "💳 شماره کارت":
        await update.message.reply_text(
            f"""💳 شماره کارت:

{CARD_NUMBER}

👤 صاحب حساب:
{CARD_OWNER}

بعد از پرداخت، رسید را برای ادمین ارسال کنید:
{ADMIN_USERNAME}
"""
        )

    elif text == "☎️ پشتیبانی":
        await update.message.reply_text(
            f"پشتیبانی:\n{ADMIN_USERNAME}"
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, menu))

    print("Bot Started...")
    app.run_polling()


if __name__ == "__main__":
    main()