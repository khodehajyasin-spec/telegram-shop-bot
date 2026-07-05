from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

TOKEN = " 8986265488:AAGXzIrE1giyjYWICplY944qbaryAD_ntSM "
from config import (
    CARD_NUMBER,
    CARD_OWNER,
    ADMIN_USERNAME,
    SHOP_NAME,
)

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
    keyboard = ReplyKeyboardMarkup(
        [
            ["🧪 تست رایگان 25MB"],
            ["📦 خرید سرویس"],
            ["🔙 بازگشت"],
        ],
        resize_keyboard=True,
    )

    await update.message.reply_text(
        "یکی از گزینه‌های زیر را انتخاب کنید:",
        reply_markup=keyboard,
    )

elif text == "🧪 تست رایگان 25MB":
    await update.message.reply_text(
        "⏳ درخواست تست شما ثبت شد.\n"
        "پس از تأیید ادمین، سرویس 25MB با اعتبار 1 ساعت برای شما ساخته می‌شود."
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