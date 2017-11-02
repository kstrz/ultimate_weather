import argparse
from crawler.main import Main
from crawler.imgw_client import get_temperature
if __name__ =='__main__':
    parser = argparse.ArgumentParser(description='Runs crawlers or IMGW client')
    parser.add_argument('--crawler', action='store_true')
    parser.add_argument('--imgw', action='store_true')

    args = parser.parse_args()

    if args.crawler:
        main = Main()
        main.process()
    if args.imgw:
        get_temperature()