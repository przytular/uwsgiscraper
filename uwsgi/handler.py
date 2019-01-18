import sys
import logging
import subprocess
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from sqlalchemy.engine import create_engine

from crawler.spiders.generic import GenericSpider

config = get_project_settings()
# hide scrapy logs
logging.getLogger('scrapy').propagate = False


def application(env, start_response):
    uri = env.get('REQUEST_URI', '').replace('/','')

    try:
        uri, params = uri.split('?')
    except ValueError:
        uri = uri
        params = ''
    with open('response.txt', 'w') as f:
        response = f.write('')
    process = subprocess.Popen(['python3', 'start.py', uri, params],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    data, logs = process.communicate()

    start_response('200 OK', [('Content-Type','application/json')])

    with open('response.txt', 'r') as f:
        response = f.read()
    return [response.encode('utf-8')]
