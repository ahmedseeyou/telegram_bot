from telegram.ext import Updater, CommandHandler
import os

# التوكن يجي من المتغير البيئي (.env ملف)
TOKEN = os.getenv("BOT_TOKEN")

def start(update, context):
    update.message.reply_text("البوت اشتغل ✅")

if __name__ == "__main__":
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()
