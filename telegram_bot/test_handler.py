
from utils.logger import get_logger

logger = get_logger(__name__)


def test(update, context):
    """Sellega käsitletakse õpilaste skripte"""
    update.message.reply_text('Katsetan sinu skripti')
    user = update['message']['chat']
    logger.info('kasutaja: ' +
                str(user['username']) + ' id: ' + str(user['id']))
    logger.info('first_name: ' +
                str(user['first_name']) + ' last_name: ' + str(user['last_name']))
    logger.info('context args: ' + str(context.args))
