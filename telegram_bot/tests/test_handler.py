import os
from utils.abi import get_folder
from utils.logger import get_logger
from tests.test_0 import test_file

logger = get_logger(__name__)

kaust = get_folder(__file__) + os.sep + 'scripts' + os.sep
os.mkdir(kaust) if not os.path.isdir(kaust) else ''

def test(update, context):
    """Sellega käsitletakse õpilaste skripte"""
    update.message.reply_text('Katsetan sinu skripti')
    user = update['message']['chat']
    logger.info('kasutaja: ' +
                str(user['username']) + ' id: ' + str(user['id']))
    logger.info('first_name: ' +
                str(user['first_name']) + ' last_name: ' + str(user['last_name']))
    logger.info('context args: ' + str(context.args))
    
    doc = update.message.document
    file_name = doc.file_name
    path = kaust + file_name
    logger.info('Downloading to: ' + path)
    context.bot.get_file(doc).download(custom_path=path)

    try:
        with open(path, 'r') as f:
            skript = f.read()
            if 'import' in skript:
                raise Exception('import pole lubatud kasutada selles ülesandes')
            if 'open' in skript:
                raise Exception('open pole lubatud kasutada selles ülesandes')
        number, nimi, grupi_number, ylesanne = scripti_tuvastamine(file_name)
        logger.info('Tuvastatud: ' + str((number, nimi, grupi_number, ylesanne)))
        print(test_file(file_name.removesuffix('.py')))
        logger.info('\033[92m Kõik hästi läbitud: ' + nimi + ' ' + grupi_number + ' ' +  ylesanne + '\033[0m')
        update.message.reply_text('JAAHHH!! Tehtud, õnnestus läbida kõiki teste')
    except Exception as exc:
        logger.info('\033[91m' + str(exc) + '\033[0m')
        update.message.reply_text(str(exc))
    except:
        update.message.reply_text('VIGA!! Tundmatu ootamatu tõrke sinu skripti katsetamises.')

def scripti_tuvastamine(fn):
    """Tagastab number, nimi, grupi_number, ylesanne kui faili nimi on õiges formaadis"""
    try:
        return fn.removesuffix('.py').removeprefix('proge').split('_')
    except:
        raise Exception('Faili nimi on vale või pole üldse Python fail')

