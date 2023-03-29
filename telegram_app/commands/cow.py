from telegram import Update
from telegram.ext import ContextTypes


async def cow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text='https://i.pinimg.com/originals/35/bb/b9/35bbb9b19f0e425013033abbeff86fb0.jpg')