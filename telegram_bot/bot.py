#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import traceback
import webbrowser
from os import getenv


from dotenv import load_dotenv, find_dotenv
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from test_handler import test
from harjutused.harjuta import harjuta
from stats.stats import register_user
from utils.logger import get_logger

# Load env data
load_dotenv(find_dotenv())
telegram_token = getenv('TELEGRAM_TOKEN')


logger = get_logger(__name__)


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Tere!')
    try:
        register_user(update['message']['chat'])
    except:
        logger.error('Could not register user. Traceback: ' +
                     traceback.format_exc())
    logger.info('Started conversation\n\t\tUpdate:\n\t\t')
    logger.info(update)
    logger.info('\n\t\Context:\n\t\t')
    logger.info(context)


def abi(update, context):
    """Send a message when the command /help is issued."""
    kaust = os.path.dirname(os.path.realpath(__file__))
    with open(kaust + os.sep + 'abi.md', 'rb') as abi_fail:
        update.message.reply_text(
            abi_fail.read().decode('utf-8'),
            parse_mode='Markdown')


def kaja(update, context):
    """Kajasta kasutaja sõnumit."""
    update.message.reply_text(update.message.text)


def brauser(update, context):
    """Rockroll õpilasi"""
    webbrowser.open('https://www.youtube.com/watch?v=2QeGa3OhRsA')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Loading telegram token from enviroment variables
    updater = Updater(
        telegram_token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("abi", abi))
    dp.add_handler(CommandHandler("kaja", kaja))
    dp.add_handler(CommandHandler("brauser", brauser))
    dp.add_handler(CommandHandler("harjuta", harjuta))
    dp.add_handler(CommandHandler("test", test, pass_user_data=True))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, kaja))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
