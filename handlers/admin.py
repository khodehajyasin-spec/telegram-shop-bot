from telegram import Update
from telegram.ext import ContextTypes

ADMIN_ID = 123456789

async def admin_panel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ دسترسی ندارید.")
        return

    await update.message.reply_text(
        "👑 پنل مدیریت\n\n"
        "📊 آمار\n"
        "👥 کاربران\n"
        "📢 پیام همگانی\n"
        "💰 سفارش‌ها\n"
        "⚙️ تنظیمات"
    )