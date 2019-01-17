# -*- coding: utf-8 -*-
import scrapy


class ItemText(scrapy.Item):
    body = scrapy.Field()


class GenericSpider(scrapy.Spider):
    name = 'generic'

    def __init__(self, connection, url_id):
        result = connection.execute('SELECT url FROM urls WHERE id={}'.format(url_id,))
        self.start_urls = [] + [r['url'] for r in result]

    def parse(self, response):
        yield ItemText(body=response.text)
