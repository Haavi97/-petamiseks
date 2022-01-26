from random import choice

from utils.abi import get_json
from utils.logger import get_logger

logger = get_logger(__name__)

harjutused = get_json('harjutused.json', script=__file__)


def harjuta(update, context):
    """Sellega käsitletakse õpilaste skripte"""
    try:
        aktsepteeritud = [0, 1, 2]
        update.message.reply_text(choice(harjutused['0' + context.args[0] + '_tase']),
                                  parse_mode='Markdown')
        kasutaja = update['message']['chat']
        logger.info('kasutaja: ' +
                    str(kasutaja['username']) + ' id: ' + str(kasutaja['id']))
    except:
        update.message.reply_text(
            'Õige tase ei olnud valitud. Aktsepteeritud: ' + str(aktsepteeritud))
        logger.info('Ei olnud õige valik. Context args: ' + str(context.args))
