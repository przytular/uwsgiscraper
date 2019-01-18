import sys
import logging
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from sqlalchemy.engine import create_engine

from crawler.spiders.generic import GenericSpider

config = get_project_settings()


def main(_id, params):
	engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
		config['DB_USER'], config['DB_PASS'], config['DB_HOST'], config['DB_PORT'], config['DB_NAME']))

	connection = engine.connect()

	process = CrawlerProcess(config)
	process.crawl(GenericSpider, connection=connection, url_id=_id, params=params)
	process.start()
	with open('response.txt') as response:
		print(response.read())

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('Please specify url ID')
		exit(1)

	_id = sys.argv[1]
	try:
		params = sys.argv[2]
	except IndexError:
		params = None
	main(_id, params)
