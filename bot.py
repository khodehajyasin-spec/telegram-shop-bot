from telegram import (
    Update,
    ReplyKeyboardMarkup,
)

from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from config import *

TOKEN = TOKEN

main_keyboard = ReplyKeyboardMarkup(
    [
        ["🧪 تست رایگان", "🛒 خرید سرویس"],
        ["📦 سرویس‌های من", "💳 پرداخت"],
        ["☎️ پشتیبانی", "🌍 Language"],
    ],
    resize_keyboard=True
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"""
👋 به {SHOP_NAME} خوش آمدید

Welcome to {SHOP_NAME}

یکی از گزینه‌های زیر را انتخاب کنید.
""",
        reply_markup=main_keyboard
    )


async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = update.message.text

    if text == "🧪 تست رایگان":

        await update.message.reply_text(
               elif text == "🇮🇷 سرور ایران":

        await update.message.reply_text(
            """
🇮🇷 سرور ایران

در نسخه نهایی:
✅ اتصال به پاسارگاد
✅ ساخت خودکار کانفیگ
✅ QR Code
✅ Subscription
"""
        )

    elif text == "🌍 سرور خارج":

        await update.message.reply_text(
            """
🌍 سرور خارج

در نسخه نهایی:
✅ اتصال به مرزبان
✅ ساخت خودکار کانفیگ
✅ QR Code
✅ Subscription
"""
        )

    elif text == "📦 سرویس‌های من":

        await update.message.reply_text(
            """
📦 سرویس‌های شما

فعلاً هیچ سرویسی ندارید.
"""
        )

    elif text == "💳 پرداخت":

        await update.message.reply_text(
            f"""
💳 شماره کارت

{CARD_NUMBER}

👤 صاحب حساب

{CARD_OWNER}

بعد از واریز، رسید پرداخت را ارسال کنید.
"""
        )

    elif text == "☎️ پشتیبانی":

        await update.message.reply_text(
            f"""
☎️ پشتیبانی

{ADMIN_USERNAME}
"""
        )

    elif text == "🌍 Language":

        language_keyboard = ReplyKeyboardMarkup(
            [
                ["🇮🇷 فارسی"],
                ["🇬🇧 English"],
                ["🔙 بازگشت"],
            ],
            resize_keyboard=True
        )

        await update.message.reply_text(
            "Select language / انتخاب زبان",
            reply_markup=language_keyboard
        )

    elif text == "🔙 بازگشت":

        await update.message.reply_text(
            "منوی اصلی",
            reply_markup=main_keyboard
        )
def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            menu
        )
    )

    print("✅ V2ray Shop Pro Started...")

    app.run_polling()


if __name__ == "__main__":
    main()