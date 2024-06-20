import configparser
import logging


def read_max_number():
    logging.info("Read configuration")
    config = configparser.ConfigParser()
    config.read('config.ini')
    max_number = config.get('settings', 'max_number')
    return int(max_number)
