import os
from telegram.ext import Updater, CommandHandler

# نجيب التوكن من متغير البيئة
TOKEN = os.getenv("TOKEN_BOT")

# دالة الرد على /start
def start(update, context):
    update.message.reply_text("هلا بيك! البوت اشتغل 🌹")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
