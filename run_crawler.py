
# run in virtual env: python ./manage.py shell < run_crawler.py

from crawler.main import Main
main = Main()
main.process()