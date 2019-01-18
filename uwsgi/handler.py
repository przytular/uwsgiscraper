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
    uri = env['REQUEST_URI']
    process = subprocess.Popen(['python3', 'start.py', uri.replace('/','')],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    data, logs = process.communicate()
    start_response('200 OK', [('Content-Type','text/html')])
    with open('response.txt') as r:
        response = r.read()
    return [response.encode('utf-8')]
