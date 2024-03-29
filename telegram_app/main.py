import logging
import os

from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from telegram_app.commands import start, cow, find_products, unknown

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    token = os.environ['TELEGRAM_TOKEN']
    app = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler('start', start)
    find_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), find_products)
    cow_handler = CommandHandler('cow', cow)

    app.add_handler(start_handler)
    app.add_handler(find_handler)
    app.add_handler(cow_handler)

    # other handlers
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    app.add_handler(unknown_handler)

    app.run_polling()
