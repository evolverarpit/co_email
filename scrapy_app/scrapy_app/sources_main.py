# coding=utf-8
import os
import sys

import pymongo

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

from scrapy_app.tasks import run_sources
from scrapy_app.settings import (
    MONGODB_HUNTER_COLLECTION,
)



def main():
    collection = db[MONGODB_HUNTER_COLLECTION]
    results = collection.find({})
    sources = []
    for company in results:
        for employee in company['employees']:
            sources.extend(employee['sources'])
    for source in sources:
        result = run_sources.delay(source)



if __name__ == '__main__':
    main()
