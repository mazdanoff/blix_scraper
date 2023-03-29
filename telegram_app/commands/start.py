from telegram import Update
from telegram.ext import ContextTypes


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