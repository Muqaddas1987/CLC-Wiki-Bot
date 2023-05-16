from telegram import Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update
from settings import settings
import requests
from telegram.ext.filters import Filters
updater = Updater(token=settings.TELEGRAM_TOKEN)
bot = updater.bot


def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello, Dear User, '
                              'Welcome to our bot!'
                              ' To search for information, '
                              'type  /search and your query.'
                              ' For example, /search Amir Temur')
    # context.bot.send_message(chat_id=update.message.chat_id, text='Hello repeatedly!')


def search(update: Update, context: CallbackContext):
    args = context.args

    if len(args) == 0:
        update.message.reply_text(' To search for entering some information, '
                                  ' For example, /search Amir Temur')
    else:
        search_text = ''.join(args)
        response = requests.get('https://en.wikipedia.org/w/api.php', {
            'action': 'opensearch',
            'search': search_text,
            'limit': 1,
            'namespace': 0,
            'format': 'json',
        })
        result = response.json()
        link = result[3]

        if len(link):
            update.message.reply_text('Link at your request:' + link[0])

        else:
            update.message.reply_text('Nothing was found for your request')


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('search', search))
dispatcher.add_handler(CommandHandler(Filters.all, start))



# bot = Bot(token="5760259279:AAERo0VwdUYZxQs4mT189vjLffelQ3Ic5gA")
# user: User = bot.get_me
# print(user)


updater.start_polling()
updater.idle()
