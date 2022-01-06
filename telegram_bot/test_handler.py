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
    logger.info('kasutaja: ' + str(user['username']) + ' id: ' + str(user['id']))
    logger.info('first_name: ' + str(user['first_name']) + ' last_name: ' + str(user['last_name']))
    logger.info('context args: ' + str(context.args))

    # {'message': {'caption_entities': [], 'entities': [{'type': 'bot_command', 'length': 6, 'offset': 0}], 'new_chat_members': [], 'supergroup_chat_created': False, 'channel_chat_created': False, 'photo': [], 'message_id': 19, 'new_chat_photo': [], 'date': 1641478844, 'delete_chat_photo': False, 'text': '/start',
    #              'chat': {'username': 'haavi97', 'id': 1446627790, 'type': 'private', 'first_name': 'Javier', 'last_name': 'Ort\xedn'}, 'group_chat_created': False, 'from': {'first_name': 'Javier', 'is_bot': False, 'username': 'haavi97', 'language_code': 'et', 'last_name': 'Ort\xedn', 'id': 1446627790}}, 'update_id': 834514635}
