import logging
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import os

TOKEN=os.environ['HAUSKUUSPOLIISI_TOKEN']
# in order to set token for bot (linux):
# export HAUSKUUSPOLIISI_TOKEN=XXXXXXXX:YYYYYYYYYYY

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="En ole vielä valmis, painu vittuun!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update.message.text) 
    print(update.message.from_user)
    print(update.message.chat)
    print(update.message_reaction)
    await update.message.reply_text(update.message.text)

def main() -> None:
    application = Application.builder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__=="__main__":
    main()
