import logging
import sys


def get_logger(skript_name):
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO,
                        handlers=[
                            logging.FileHandler('debug.log'),
                            logging.StreamHandler(sys.stdout)
                        ])
    return logging.getLogger(skript_name)
