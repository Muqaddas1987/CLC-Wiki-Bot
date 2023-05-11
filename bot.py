from telegram import Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update
from settings import settings

updater = Updater(token=settings.TELEGRAM_TOKEN)
bot = updater.bot


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello')
    context.bot.send_message(chat_id=update.message.chat_id, text='Hello repeatedly!')


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
# bot = Bot(token="5760259279:AAERo0VwdUYZxQs4mT189vjLffelQ3Ic5gA")
# user: User = bot.get_me
# print(user)


updater.start_polling()
updater.idle()
