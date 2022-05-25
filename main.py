from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup,Message, Bot
from Config import TOKEN
from Text import START_MESSAGE, HELP_TEXT
import logging
import Text
 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)

LOGGER.info("bot succesfully started")
updater = Updater(token=TOKEN, use_context=True)
dp = updater.dispatcher
users_id =[]
keyboard = InlineKeyboardMarkup(
    [
    [InlineKeyboardButton("📬Channel ", url='https://t.me/goodwayshop'),
    InlineKeyboardButton("help", callback_data='get_help'),
    ],
    [InlineKeyboardButton("➕ Add group", url= f"http://t.me/generator01_bot?startgroup=new")],
    ]
)

   
def start(update: Update, context: CallbackContext):
    user = update.effective_user.first_name
    
    update.message.reply_text(START_MESSAGE.format( bot_name=dp.bot.first_name,user_name=user),
                            reply_markup=keyboard,
                            parse_mode='html')
    ids = update.effective_user.id
    users_id.append(ids)
    LOGGER.info("runnning succesfully without error")

def get_id(update: Update, context: CallbackContext):
    yours_ids = update.effective_user.id
    chat_id = update.effective_chat.id
    if update.effective_chat.type == "private":
        update.message.reply_text(text ="Your id : {}".format(yours_ids ), quote = True)
    else:
        update.message.reply_text(text = "This chat\'s id is : {}".format(chat_id))



def help(update:Update, context:CallbackContext):
    update.message.reply_text(Text.HELP_TEXT)
    LOGGER.info("runnning succesfully without error")

def get_help(update:Update, context:CallbackContext):
    query = update.callback_query
    query.answer()
    query.edit_message_text(Text.HELP_TEXT,reply_markup=keyboard)
    LOGGER.info("Callback data runnning succesfully without error")

def broadcast( update:Update, context:CallbackContext):
    message = update.effective_message.text
    
    for id in users_id:
        message.reply_text(text = message, chat_id = id)



dp.add_handler(CommandHandler('start', start))

dp.add_handler(CommandHandler('help',help))
dp.add_handler(CommandHandler('id',get_id))
dp.add_handler(CommandHandler('broadcast',broadcast))
dp.add_handler(CallbackQueryHandler(get_help))



updater.start_polling()
updater.idle()

