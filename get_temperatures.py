import argparse
import os
import sys
from datetime import datetime
from crawler.main import Main
from crawler.imgw_client import get_temperature
import logging

if __name__ =='__main__':
    parser = argparse.ArgumentParser(description='Runs crawlers or IMGW client')
    parser.add_argument('--crawler', action='store_true')
    parser.add_argument('--imgw', action='store_true')

    args = parser.parse_args()
    if args.crawler:
        logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), 'log', 'crawler.log'), level=logging.INFO)
        logging.info('START CRAWLER ' + str(datetime.utcnow()))
        main = Main()
        main.process()
    if args.imgw:
        logging.basicConfig(filename=os.path.join(os.path.dirname(__file__), 'log', 'imgw.log'), level=logging.INFO)
        logging.info('START IMGW CLIENT ' + str(datetime.utcnow()))
        get_temperature()
