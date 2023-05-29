from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def start(update, context):
    keyboard = [[InlineKeyboardButton("Тык", callback_data='1'),
                 InlineKeyboardButton("Тык 2", callback_data='2')],
                [InlineKeyboardButton("Тык 3", callback_data='3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Button {} selected".format(query.data))

token = '5848466467:AAFNMiwaH7KlckhCotqOmteMhZLDA0SBBLk'
updater = Updater(token, use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

updater.start_polling()
updater.idle()