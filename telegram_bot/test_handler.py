import logging
import sys

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    handlers=[
                        logging.FileHandler("debug.log"),
                        logging.StreamHandler(sys.stdout)
                    ])

logger = logging.getLogger(__name__)


def test(update, context):
    """Sellega käsitletakse õpilaste skripte"""
    update.message.reply_text('Katsetan sinu skripti')
    user = update['message']['chat']
    logger.info('kasutaja: ' +
                str(user['username']) + ' id: ' + str(user['id']))
    logger.info('first_name: ' +
                str(user['first_name']) + ' last_name: ' + str(user['last_name']))
    logger.info('context args: ' + str(context.args))
