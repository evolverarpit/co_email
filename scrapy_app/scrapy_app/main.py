# coding=utf-8
import os
import sys

import pymongo

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from hunter.settings import URL_FILES
from hunter.tasks import run_spider
from hunter.utils import get_urls



def Hunter():
    for file in URL_FILES:
        urls = get_urls(file)
        result = run_spider.delay('hunter', urls)


if __name__ == '__main__':
    Hunter()
