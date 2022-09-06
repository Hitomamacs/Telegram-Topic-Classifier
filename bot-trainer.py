import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update, ParseMode
import pickle
from os.path import exists
import time

telegram_token=<ADD HERE THE TELEGRAM BOT TOKEN>
senderbot = telegram.Bot(token=telegram_token)
updater = Updater(token=telegram_token, use_context=True, user_sig_handler=True)
dispatcher = updater.dispatcher

with open('./tagged_db.pickle', 'rb') as f:
    dataset = pickle.load(f)

button_list = []
for topic in ["matematica", "fisica", "chimica", "informatica", "biologia", "geologia", "filosofia", "nessuno"]:
    button_list.append([InlineKeyboardButton(topic, callback_data=topic)])
select_keyboard = InlineKeyboardMarkup(button_list)

def image(update, context, from_keyboard=False):
    global dataset
    with open('./tagged_db.pickle', 'rb') as f:
        dataset = pickle.load(f)
    if from_keyboard:
        chat_id = update['callback_query']['message']['chat']['id']
    else:
        chat_id = update['message']['chat']['id']

    for img_hash in dataset:
        if dataset[img_hash]['topic']:
            continue
        else:
            break

    counter = 0
    for i in dataset:
        if  not dataset[i]['topic']:
            counter+=1

    senderbot.sendMessage(chat_id=chat_id, text="Images to go: "+str(counter))
    senderbot.sendPhoto(chat_id, photo=open('./training/'+dataset[img_hash]['filename'], 'rb'))
    senderbot.sendMessage(chat_id=chat_id, text=img_hash, reply_markup=select_keyboard)

def topic_selected(update, context):
    global dataset
    query = update.callback_query
    dataset[query.message.text]['topic']=query.data
    with open('./tagged_db.pickle', 'wb') as f:
        pickle.dump(dataset, f, protocol=pickle.HIGHEST_PROTOCOL)
    image(update, context, True)

dispatcher.add_handler(CommandHandler("start", image))
dispatcher.add_handler(CallbackQueryHandler(topic_selected))
updater.start_polling()
