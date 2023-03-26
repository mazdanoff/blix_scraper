import asyncio
import logging
from os import environ

from telegram import Update, InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters, InlineQueryHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=f"Hello, {name}!\n"
                                        f"I'm Bliksik, and my purpose is to help you find the best sales "
                                        f"for your desired products.\n\n"
                                        f"Currently though, I'm in the middle of being developed, so my capabilities "
                                        f"are still limited.\n\n"
                                        f"Right now, I'll repeat every message you write to me, unless it's a command.\n"
                                        f"You can try out a few commands to get a glimpse of what I can do in the future.\n"
                                        f"Try out these:\n"
                                        f"-> /caps <sentence_that_will_be_returned_capitalized>\n"
                                        f"-> /whatsmyname"
                                        f"-> /cow\n\n"
                                        f"Have a nice day and please be patient!")


async def whats_my_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"As far as I know, your name is {name}!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


async def caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_in_caps = ' '.join(context.args).upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_in_caps)


async def cow(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text='https://i.pinimg.com/originals/35/bb/b9/35bbb9b19f0e425013033abbeff86fb0.jpg')


async def inline_caps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    await context.bot.answer_inline_query(update.inline_query.id, results)


async def find_products(search_phrase: str):
    await asyncio.sleep(5)
    return dict(
        name="Napój owsiany GoVege",
        price="3,75 zł",
        store="Biedronka",
        time="30 luty - 31 luty",
        img_link="https://cdn.biedronka.pl/newsletter/assets-glovo/_cz03/360563.jpg"
    )


async def test_products(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phrase = "-".join(context.args)
    msg = await context.bot.send_message(chat_id=update.effective_chat.id,
                                         text=f'Searching Blix for {" ".join(context.args)}...')
    result = await find_products(phrase)
    await context.bot.delete_message(chat_id=msg.chat_id, message_id=msg.id)
    new_msg = f"{result['name']}, {result['price']}\n" \
              f"{result['store']}, {result['time']}\n" \
              f"{result['img_link']}"
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text=new_msg)


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

if __name__ == '__main__':
    token = environ['TELEGRAM_TOKEN']
    app = ApplicationBuilder().token(token).build()

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    caps_handler = CommandHandler('caps', caps)
    cow_handler = CommandHandler('cow', cow)
    whats_my_name_handler = CommandHandler('whatsmyname', whats_my_name)
    inline_caps_handler = InlineQueryHandler(inline_caps)
    test_products_handler = CommandHandler('find', test_products)

    app.add_handler(start_handler)
    app.add_handler(echo_handler)
    app.add_handler(caps_handler)
    app.add_handler(cow_handler)
    app.add_handler(whats_my_name_handler)
    app.add_handler(inline_caps_handler)
    app.add_handler(test_products_handler)

    # other handlers
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    app.add_handler(unknown_handler)

    app.run_polling()
