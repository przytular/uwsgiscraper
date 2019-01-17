import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from sqlalchemy.engine import create_engine

from crawler.spiders.generic import GenericSpider

config = get_project_settings()


def main(_id):
	engine = create_engine('mysql+mysqldb://{}:{}@{}:{}/{}'.format(
		config['DB_USER'], config['DB_PASS'], config['DB_HOST'], config['DB_PORT'], config['DB_NAME']))

	connection = engine.connect()

	process = CrawlerProcess(config)
	process.crawl(GenericSpider, connection=connection, url_id=_id)
	process.start()


if __name__ == '__main__':
	try:
		_id = sys.argv[1]
		main(_id)
	except IndexError:
		print('Please specify url ID')
		exit(1)
