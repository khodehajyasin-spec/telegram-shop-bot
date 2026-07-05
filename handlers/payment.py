from telegram import Update
from telegram.ext import ContextTypes

async def payment_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💳 روش پرداخت\n\n"
        "فعلاً فقط کارت‌به‌کارت فعال است.\n\n"
        "بعد از واریز، رسید را ارسال کنید."
    )

async def receive_receipt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        await update.message.reply_text(
            "✅ رسید شما دریافت شد.\n"
            "پس از بررسی توسط ادمین، سرویس ساخته می‌شود."
        )