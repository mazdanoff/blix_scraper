import logging
import os

from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from telegram_app.commands import start, cow, find_products, unknown
from telegram_app.message_handling.echo import echo

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    token = os.environ['TELEGRAM_TOKEN']
    app = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    cow_handler = CommandHandler('cow', cow)
    find_handler = CommandHandler('find', find_products)

    app.add_handler(start_handler)
    app.add_handler(echo_handler)
    app.add_handler(cow_handler)
    app.add_handler(find_handler)

    # other handlers
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    app.add_handler(unknown_handler)

    app.run_polling()
