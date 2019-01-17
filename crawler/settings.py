# -*- coding: utf-8 -*-

BOT_NAME = 'crawler'
SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'
ROBOTSTXT_OBEY = False

USER_AGENT = 'crawler'

ITEM_PIPELINES = {
   'crawler.pipelines.ItemCollectorPipeline': 300,
}

DB_USER = 'scraper'
DB_PASS = 'scraper'
DB_NAME = 'scraper'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
