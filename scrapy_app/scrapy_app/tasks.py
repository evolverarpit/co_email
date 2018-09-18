# coding=utf-8
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from scrapy.crawler import CrawlerProcess
from billiard import Process
from scrapy.utils.project import get_project_settings
#from scrapy_app import app
from scrapy.settings import Settings


class HunterCrawler(Process):
    def __init__(self, spider, urls):
        Process.__init__(self)
        settings = Settings()
        self.crawler = CrawlerProcess(settings)
        self.urls = urls
        self.spider = spider

    def run(self):
        if self.spider == 'hunter':
            from scrapy_app.spiders import Hunter
            self.crawler.crawl(Hunter, self.urls)
        elif self.spider == 'sources':
            from scrapy_app.spiders import Sources
            self.crawler.crawl(Sources, self.urls)
        self.crawler.start()


def run_spider(spider, urls):
    crawler = HunterCrawler(spider, urls)
    crawler.start()
    crawler.join()

