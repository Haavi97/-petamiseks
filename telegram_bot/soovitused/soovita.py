from random import choice

from utils.abi import get_json, dump_json
from utils.logger import get_logger

logger = get_logger(__name__)

soovitused = get_json('soovitused.json', script=__file__)


def soovita(update, context):
    """Sellega käsitletakse õpilaste soovitusi"""
    update.message.reply_text('Aitäh soovituse eest!')
    soovitus = ' '.join(context.args)
    kasutaja = update['message']['chat']
    soovitused['soovitused'].append({'soovitab': kasutaja['username'],
                                     'kasutaja_id': kasutaja['id'], 'soovitus': soovitus})
    logger.info('kasutaja: ' +
                str(kasutaja['username']) + ' id: ' + str(kasutaja['id']) + 'soovitus: ' + soovitus)

    dump_json(soovitused, 'soovitused.json', script=__file__)
