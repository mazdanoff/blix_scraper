from selenium.common import WebDriverException
from telegram import Update
from telegram.ext import ContextTypes

from scripts.driver import Driver
from telegram_app.get_sales import get_sales


async def find_products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = await context.bot.send_message(chat_id=update.effective_chat.id,
                                         text=f'Searching Blix for {" ".join(context.args)}...')
    phrase = "-".join(context.args)
    try:
        with Driver() as driver:
            for sale in get_sales(driver, phrase):
                await context.bot.send_message(chat_id=update.effective_chat.id,
                                               text=str(sale))
                await context.bot.delete_message(chat_id=msg.chat_id, message_id=msg.id)
                msg = await context.bot.send_message(chat_id=update.effective_chat.id,
                                                     text=f'Searching Blix for further results...')
    except WebDriverException:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="An error has occurred.\nPlease contact your nearest household developer.")

    await context.bot.delete_message(chat_id=msg.chat_id, message_id=msg.id)