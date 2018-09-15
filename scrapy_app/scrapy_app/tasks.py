# coding=utf-8
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from billiard import Process
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy_app import app

settings = get_project_settings()


class HunterProcess(Process):
    def __init__(self, url):
        Process.__init__(self)
        self.crawler = CrawlerProcess(get_project_settings())
        self.url = url

    def run(self):
        from scrapy_app.spiders import Hunter
        self.crawler.crawl(Hunter, self.url)
        self.crawler.start()


class SourcesProcess(Process):
    def __init__(self, url):
        Process.__init__(self)
        self.crawler = CrawlerProcess(get_project_settings())
        self.url = url

    def run(self):
        from scrapy_app.spiders import Sources
        self.crawler.crawl(Sources, self.url)
        self.crawler.start()


@app.task(name='crawler.scrapy_app.tasks.run_spider')
def run_spider(url):
    crawler = HunterProcess(url)
    crawler.start()
    crawler.join()


@app.task(name='crawler.scrapy_app.tasks.run_sources')
def run_sources(url):
    crawler = SourcesProcess(url)
    crawler.start()
    crawler.join()
