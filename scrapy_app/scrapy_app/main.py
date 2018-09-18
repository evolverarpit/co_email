# coding=utf-8
import os
import sys

import pymongo

sys.path.append(os.path.dirname(os.path.abspath('.')))

#from scrapy_app.settings import URL_FILES
from scrapy_app.tasks import run_spider
#from scrapy_app.utils import get_urls


URL_FILES = ['https://hunter.io/companies/letters/0/1/','https://hunter.io/companies/letters/1/1/','https://hunter.io/companies/letters/2/1/','https://hunter.io/companies/letters/3/1/','https://hunter.io/companies/letters/4/1/','https://hunter.io/companies/letters/5/1/','https://hunter.io/companies/letters/6/1/','https://hunter.io/companies/letters/7/1/','https://hunter.io/companies/letters/8/1/','https://hunter.io/companies/letters/9/1/','https://hunter.io/companies/letters/a/1/','https://hunter.io/companies/letters/b/1/','https://hunter.io/companies/letters/c/1/','https://hunter.io/companies/letters/d/1/','https://hunter.io/companies/letters/e/1/','https://hunter.io/companies/letters/f/1/','https://hunter.io/companies/letters/g/1/','https://hunter.io/companies/letters/h/1/','https://hunter.io/companies/letters/i/1/','https://hunter.io/companies/letters/j/1/','https://hunter.io/companies/letters/k/1/','https://hunter.io/companies/letters/l/1/','https://hunter.io/companies/letters/m/1/','https://hunter.io/companies/letters/n/1/','https://hunter.io/companies/letters/o/1/','https://hunter.io/companies/letters/p/1/','https://hunter.io/companies/letters/q/1/','https://hunter.io/companies/letters/r/1/','https://hunter.io/companies/letters/s/1/','https://hunter.io/companies/letters/t/1/','https://hunter.io/companies/letters/u/1/','https://hunter.io/companies/letters/v/1/','https://hunter.io/companies/letters/w/1/','https://hunter.io/companies/letters/x/1/','https://hunter.io/companies/letters/y/1/','https://hunter.io/companies/letters/z/1/']
def Hunter():
    #for file in URL_FILES:
        #urls = get_urls(file)
    result = run_spider('hunter', URL_FILES)


if __name__ == '__main__':
    Hunter()

