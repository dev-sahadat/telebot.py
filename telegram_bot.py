from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# স্টার্ট কমান্ডের জন্য হ্যান্ডলার
def start(update, context):
    update.message.reply_text("হ্যালো! আমি একটি টেলিগ্রাম বট। আপনার কী সাহায্য করতে পারি?")

# মেসেজের জন্য হ্যান্ডলার
def echo(update, context):
    update.message.reply_text(update.message.text)

# মূল প্রোগ্রাম
def main():
    # এখানে আপনার বটের টোকেনটি দিন
    TOKEN = '7487129279:AAHsRPCAp0LgdGTYrcaakJ258ApaDW0Egr8'
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    # কমান্ড হ্যান্ডলার যোগ করুন
    dp.add_handler(CommandHandler("start", start))

    # মেসেজ হ্যান্ডলার যোগ করুন
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # বটটি চালু করুন
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
