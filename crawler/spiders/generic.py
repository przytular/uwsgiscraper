# -*- coding: utf-8 -*-
import scrapy


class ItemText(scrapy.Item):
    body = scrapy.Field()


class GenericSpider(scrapy.Spider):
    name = 'generic'

    def __init__(self, connection, url_id, params=None):
        request_parameters = {}
        if params:
            list_of_params = [ param.split('=') for param in params.split('&')]
            for p in list_of_params:
                try:
                    request_parameters[p[0]] = p[1]
                except IndexError:
                    pass
        self.request_parameters = request_parameters

        result = connection.execute('SELECT url FROM urls WHERE id={}'.format(int(url_id),))
        self.start_urls = [] + [r['url'] for r in result]

    def parse(self, response):
        yield ItemText(body=response.text)
