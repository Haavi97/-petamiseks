import logging
import os
import sys
import json
from random import choice

from utils.abi import get_json

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    handlers=[
                        logging.FileHandler('debug.log'),
                        logging.StreamHandler(sys.stdout)
                    ])

logger = logging.getLogger(__name__)

harjutused = get_json('harjutused.json', script=__file__)


def harjuta(update, context):
    """Sellega käsitletakse õpilaste skripte"""
    if '0' in context.args:
        update.message.reply_text(choice(harjutused['00_tase']))
        kasutaja = update['message']['chat']
        logger.info('kasutaja: ' +
                    str(kasutaja['username']) + ' id: ' + str(kasutaja['id']))
    else:
        update.message.reply_text('Õige tase ei olnud valitud')
        logger.info('Ei olnud õige valik. Context args: ' + str(context.args))
