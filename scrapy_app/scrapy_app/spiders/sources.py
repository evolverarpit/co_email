# coding=utf-8
import re

import requests
import scrapy
from scrapy_app.items import SourceItem
from scrapy_app.settings import PROXIES, USER_AGENT_LIST
from scrapy.linkextractors import LinkExtractor


class Sources(scrapy.Spider):
    "Scraper to scrape html sources"
    
    def __init__(self, url='', **kwargs):
        self.proxy_pool = PROXIES
        self.USER_AGENT_LIST = USER_AGENT_LIST
        self.start_urls = [url, ]
        super(Sources, self).__init__(**kwargs)

    name = 'sources'

    def parse(self, response):
        source = SourceItem()
        data = requests.get(response.url).text
        links = LinkExtractor().extract_links(response=response)
        source['url'] = response.url
        source['links'] = [link.url for link in links]
        source['html'] = data
        source['emails'] = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', data)
        yield source
