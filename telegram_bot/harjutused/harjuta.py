import logging
import os
import sys
import json
from random import choice

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    handlers=[
                        logging.FileHandler("debug.log"),
                        logging.StreamHandler(sys.stdout)
                    ])

logger = logging.getLogger(__name__)

kaust = os.path.dirname(os.path.realpath(__file__))
f = open(kaust + os.sep + 'harjutused.json')
harjutused = json.load(f)


def harjuta(update, context):
    """Sellega käsitletakse õpilaste skripte"""
    if '0' in context.args:
        update.message.reply_text(choice(harjutused['00_tase']))
        user = update['message']['chat']
        logger.info('kasutaja: ' +
                    str(user['username']) + ' id: ' + str(user['id']))
    else:
        update.message.reply_text('Õige tase ei olnud valitud')
        logger.info('Ei olnud õige valik. Context args: ' + str(context.args))
